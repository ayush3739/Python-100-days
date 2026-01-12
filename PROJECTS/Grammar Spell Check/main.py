from flask import Flask, request, render_template, jsonify
import json
from pathlib import Path
import os, time
import requests

from stock import stocks_comp, stock_call, stock_fetch, check_dates

app = Flask(__name__)

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

_NONWATCHLIST_LAST_REFRESH = {}

def _nonwatchlist_cooldown_remaining_seconds(symbol: str, cooldown_hours: int = 6) -> int:
    last = _NONWATCHLIST_LAST_REFRESH.get(symbol)
    if not last:
        return 0
    remaining = int(cooldown_hours * 3600 - (time.time() - last))
    return remaining if remaining > 0 else 0

def _load_global_quotes():
    path = Path(__file__).resolve().parent / "Global_Quotes.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def _global_quotes_path() -> Path:
    return Path(__file__).resolve().parent / "Global_Quotes.json"

def _update_global_quotes(symbol: str, global_quote: dict) -> None:
    path = _global_quotes_path()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f) or {}
    except FileNotFoundError:
        data = {}
    data[symbol] = global_quote
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def _refresh_global_quote(symbol: str) -> bool:
    api_key = os.getenv("API_KEY")
    if not api_key:
        return False

    params = {
        "apikey": api_key,
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "datatype": "json",
    }
    resp = requests.get(STOCK_ENDPOINT, params=params, timeout=30)
    resp.raise_for_status()
    payload = resp.json() or {}

    if "Note" in payload or "Error Message" in payload or "Information" in payload:
        return False

    quote = payload.get("Global Quote")
    if not isinstance(quote, dict) or not quote.get("01. symbol"):
        return False

    _update_global_quotes(symbol, quote)
    return True

@app.route("/stock/<symbol>")
def stock(symbol):
    symbol = (symbol or "").strip().upper()

    if symbol in stocks_comp:
        stock_data = check_dates(symbol)
        if not stock_data:
            stock_data = stock_call(symbol)
    else:
        stock_data = stock_fetch(symbol)

    if "Time Series (Daily)" not in stock_data:
        return jsonify({"error": "No daily time series data available", "symbol": symbol, "raw": stock_data}), 502

    try:
        days = int(request.args.get("days", 60))
    except ValueError:
        days = 60
    if days not in (30, 60, 90):
        days = 60

    daily = stock_data["Time Series (Daily)"]
    dates = list(daily.keys())[:days]
    closes = [float(daily[d]["4. close"]) for d in dates]
    volume = [int(daily[d]["5. volume"]) for d in dates]

    dates.reverse()
    closes.reverse()
    volume.reverse()

    return jsonify({"dates": dates, "closes": closes ,"volume":volume})

@app.route('/')
def home():
    quotes = _load_global_quotes()

    selected_symbol = (request.args.get("symbol") or (stocks_comp[0] if stocks_comp else "")).strip().upper()
    selected_quote = quotes.get(selected_symbol) if isinstance(quotes, dict) else None

    return render_template(
        "index.html",
        stock_list=stocks_comp,
        selected_symbol=selected_symbol,
        selected_quote=selected_quote,
        symbol_supported=True,
    )

def _cache_path(symbol: str) -> Path:
    return Path("cache") / f"{symbol}.json"

def _cooldown_remaining_seconds(symbol: str, cooldown_hours: int = 6) -> int:
    p = _cache_path(symbol)
    if not p.exists():
        return 0
    age = time.time() - os.path.getmtime(p)
    remaining = int(cooldown_hours * 3600 - age)
    return remaining if remaining > 0 else 0

@app.post("/refresh")
def refresh():
    data = request.get_json(silent=True) or {}
    symbol = ((data.get("symbol") or "").strip().upper())

    if not symbol:
        return jsonify({"error": "Missing symbol"}), 400

    if symbol in stocks_comp:
        cached = check_dates(symbol)
        if cached:
            quote_updated = False
            try:
                quote_updated = _refresh_global_quote(symbol)
            except Exception:
                quote_updated = False

            remaining = _cooldown_remaining_seconds(symbol, cooldown_hours=6)
            return jsonify({
                "ok": True,
                "symbol": symbol,
                "status": "already_latest",
                "message": "Data is already latest. No refresh needed.",
                "retry_after_seconds": remaining,
                "global_quote_updated": quote_updated
            })

        remaining = _cooldown_remaining_seconds(symbol, cooldown_hours=6)
        if remaining > 0:
            return jsonify({"error": "Cooldown active", "symbol": symbol, "retry_after_seconds": remaining}), 429

        fresh = stock_call(symbol)
        if "Time Series (Daily)" not in fresh:
            return jsonify({"error": "Fetch failed", "symbol": symbol, "raw": fresh}), 502

        quote_updated = False
        try:
            quote_updated = _refresh_global_quote(symbol)
        except Exception:
            quote_updated = False

        return jsonify({
            "ok": True,
            "symbol": symbol,
            "status": "updated",
            "message": "Data has been updated.",
            "global_quote_updated": quote_updated
        })

    remaining = _nonwatchlist_cooldown_remaining_seconds(symbol, cooldown_hours=6)
    if remaining > 0:
        return jsonify({"error": "Cooldown active", "symbol": symbol, "retry_after_seconds": remaining}), 429

    fresh = stock_fetch(symbol)
    if "Time Series (Daily)" not in fresh:
        return jsonify({"error": "Fetch failed", "symbol": symbol, "raw": fresh}), 502

    _NONWATCHLIST_LAST_REFRESH[symbol] = time.time()

    quote_updated = False
    try:
        quote_updated = _refresh_global_quote(symbol)
    except Exception:
        quote_updated = False

    return jsonify({
        "ok": True,
        "symbol": symbol,
        "status": "updated",
        "message": "Data has been updated.",
        "global_quote_updated": quote_updated
    })

@app.get("/search")
def search():
    keywords = (request.args.get("keywords") or "").strip()
    if not keywords:
        return jsonify({"matches": []})

    api_key = os.getenv("API_KEY")
    if not api_key:
        return jsonify({"error": "Missing API_KEY"}), 500

    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": keywords,
        "apikey": api_key,
        "datatype": "json",
    }

    resp = requests.get(STOCK_ENDPOINT, params=params, timeout=30)
    resp.raise_for_status()
    payload = resp.json() or {}

    if "Note" in payload or "Error Message" in payload or "Information" in payload:
        return jsonify({"error": "Search temporarily unavailable", "raw": payload}), 503

    best = payload.get("bestMatches") or []
    matches = []
    for m in best[:10]:
        matches.append({
            "symbol": m.get("1. symbol", ""),
            "name": m.get("2. name", ""),
            "region": m.get("4. region", ""),
            "currency": m.get("8. currency", ""),
            "score": m.get("9. matchScore", ""),
        })

    return jsonify({"matches": matches})

if __name__ == "__main__":
    app.run(debug=True)
