# Habit Tracker with Pixela API

A GUI application for tracking daily habits using the Pixela API service with a beautiful calendar interface.

## Features
- Interactive calendar widget for date selection
- Add daily habit data (hours/quantity)
- Update existing entries
- Delete habit records
- Visual habit tracking graph via Pixela
- Tkinter GUI with custom styling

## Files
- `main.py` - Main GUI application
- `API PIXELA.ipynb` - Jupyter notebook with API examples
- `snorlax.png` - Application icon
- `.env` - Environment variables (not included)

## How to Use
1. Set up Pixela account and get API credentials
2. Create `.env` file with:
   ```
   TOKEN=your_pixela_token
   GraphID=your_graph_id
   ```
3. Run `main.py`
4. Select date from calendar
5. Enter hours/quantity for that day
6. Use Add/Update/Delete buttons as needed
7. Click "Show Journey" to view your habit graph online

## API Operations Demonstrated
- POST: Add new pixel data
- PUT: Update existing pixel data  
- DELETE: Remove pixel data
- Graph visualization through web interface

## Requirements
- Python 3.x
- tkinter (built-in)
- tkcalendar
- requests
- python-dotenv
- Pixela account and API access
