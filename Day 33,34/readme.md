# API Integration & ISS Tracker

A collection of API integration projects including ISS (International Space Station) tracking, sunrise/sunset times, and Kanye West quotes.

## Features
- **ISS Position Tracking**: Real-time International Space Station location monitoring
- **Email Notifications**: Automated email alerts when ISS is overhead
- **Sunrise/Sunset API**: Day/night cycle detection for your location
- **Kanye Quotes API**: Random Kanye West quote generator
- **Location-based Services**: GPS coordinate integration
- **Automated Scheduling**: Continuous monitoring capabilities

## ISS Tracker Functionality
1. **Position Checking**: Monitors ISS location via API
2. **Proximity Detection**: Alerts when ISS is within ±5 degrees of your location
3. **Day/Night Detection**: Checks if it's dark enough to see the ISS
4. **Email Alerts**: Sends notification emails when conditions are perfect
5. **Continuous Monitoring**: Runs in background checking every 60 seconds

## API Integrations
- **ISS Location API**: `http://api.open-notify.org/iss-now.json`
- **Sunrise/Sunset API**: `https://api.sunrise-sunset.org/json`
- **Email SMTP**: Gmail integration for notifications
- **Kanye Quotes**: Random quote API integration

## Files
- `main.py` - Main ISS tracker and notification system
- `sunrise & sunset api.py` - Sunrise/sunset time calculator
- `config.py` - Configuration file for API keys and settings
- `kanye-quotes-start/` - Kanye quotes API project

## Configuration Setup
Update the following in your code:
```python
my_email = "Your mail here"
passw = "Your pass_key"  # Gmail app password
MY_LAT = 'Your latitude'  # Your GPS latitude
MY_LONG = 'Your longitude'  # Your GPS longitude
```

## How ISS Tracking Works
1. **Fetch ISS Position**: GET request to ISS API
2. **Compare Coordinates**: Check if ISS is within viewing range
3. **Check Time**: Determine if it's dark enough to see ISS
4. **Send Alert**: Email notification if both conditions met
5. **Repeat**: Continue monitoring every 60 seconds

## Email Alert Features
- **Conditional Sending**: Only sends when ISS is visible
- **Night Detection**: Ensures it's dark enough for viewing
- **SMTP Integration**: Uses Gmail for reliable delivery
- **Automated Scheduling**: Runs continuously in background

## Learning Concepts
- **API Integration**: HTTP requests and JSON processing
- **Email Automation**: SMTP protocol and email sending
- **Time/Date Handling**: Working with datetime and timezones
- **Geographic Calculations**: Latitude/longitude comparisons
- **Error Handling**: API response validation
- **Continuous Processing**: Background task implementation

## Requirements
- Python 3.x
- requests library
- smtplib (included with Python)
- Gmail account with app password
- Your GPS coordinates

## Installation
```bash
pip install requests
python main.py
```

## API Services Used
- **Open Notify ISS API**: Free ISS location tracking
- **Sunrise Sunset API**: Free sunrise/sunset calculations
- **Gmail SMTP**: Email delivery service
- **Kanye West Quotes API**: Fun quote generation

## Customization Ideas
- Add weather condition checking
- Include moon phase information
- Send SMS notifications instead of email
- Add multiple location monitoring
- Create web dashboard for tracking
- Include satellite pass predictions

Perfect for learning API integration while building a practical astronomy notification system!