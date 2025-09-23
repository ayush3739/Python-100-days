# Automatic Rain Alert System

A weather monitoring system that sends WhatsApp alerts when rain is expected in your area.

## Features
- Fetches weather forecast using OpenWeatherMap API
- Monitors next 12 hours for rain conditions
- Sends WhatsApp notifications via Twilio API
- Uses environment variables for secure credential storage
- Saves weather data to JSON file for reference

## How It Works
1. Gets weather forecast for specified coordinates
2. Checks if any weather condition indicates rain (ID < 700)
3. If rain detected, sends WhatsApp message with umbrella reminder
4. Weather data is saved locally for debugging

## Setup
1. Create `.env` file with required credentials:
   ```
   API_KEY=your_openweathermap_api_key
   ACCOUNT_ID=your_twilio_account_id
   auth_token=your_twilio_auth_token
   lat=your_latitude
   lon=your_longitude
   ```
2. Install required packages:
   ```bash
   pip install requests python-dotenv twilio
   ```

## Configuration
- Update WhatsApp numbers in the script
- Set your location coordinates in `.env` file
- Customize the alert message as needed

## Requirements
- Python 3.x
- OpenWeatherMap API key
- Twilio account for WhatsApp messaging
- requests, python-dotenv, twilio packages
