# Day 49 - Automated Gym Class Booking Bot

## Overview
An advanced Selenium-based automation bot that automatically books gym classes based on specific criteria. This project demonstrates complex web automation with error handling, retry logic, and verification mechanisms.

## Project Description

### Gym Booking Bot (main.py & step1.py)
A sophisticated automation system that:
- Logs into a gym booking platform
- Searches for specific classes (Tuesday and Thursday 6:00 PM classes)
- Automatically books available classes
- Joins waitlists when classes are full
- Verifies bookings on the "My Bookings" page
- Implements network resilience with retry mechanisms

**Key Features:**
- **Automated Login**: Secure login with credentials from environment variables
- **Smart Class Selection**: Filters classes by day (Tue/Thu) and time (6:00 PM)
- **Multiple Booking States**: Handles "Book Class", "Waitlist", "Booked", and "Waitlisted" states
- **Network Resilience**: Retry logic with up to 7 attempts for network issues
- **Chrome Profile Management**: Uses custom Chrome profile for persistent sessions
- **Verification System**: Validates all bookings on the My Bookings page
- **Detailed Reporting**: Provides comprehensive status updates and counts

## Technical Implementation

### Retry Mechanism
```python
def retry(func, retries=7, description=None):
    # Implements automatic retry with timeout handling
```

### Key Functionalities
1. **Login Process**: Automated login with explicit waits
2. **Class Booking**: Intelligent booking with state management
3. **Waitlist Joining**: Automatic waitlist registration
4. **Verification**: Cross-checks bookings on dedicated page

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Python 3**: Programming language
- **Chrome WebDriver**: Chrome browser with custom profile
- **WebDriverWait**: Explicit waits for reliable automation
- **Exception Handling**: TimeoutException, NoSuchElementException

## Configuration

### Required Credentials
```python
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"
```

### Chrome Profile Setup
- Creates and uses a custom Chrome profile for persistent sessions
- Keeps browser open with `detach` option
- Custom user data directory for session management

## Prerequisites
```bash
pip install selenium
```

## Setup
1. Install Selenium: `pip install selenium`
2. Update `ACCOUNT_EMAIL` and `ACCOUNT_PASSWORD` in the script
3. Create a manual account first on the gym website
4. Ensure Chrome browser is installed

## Usage

### Run the Booking Bot
```bash
python main.py
```

### Step-by-Step Version
```bash
python step1.py
```

## Features Breakdown

### 1. Login Automation
- Clicks login button
- Fills email and password fields
- Submits login form
- Waits for schedule page to load

### 2. Class Selection Logic
- Filters by specific days (Tuesday, Thursday)
- Filters by specific time (6:00 PM)
- Checks button states before action

### 3. Booking Actions
- **Book Class**: For available classes
- **Join Waitlist**: For full classes
- **Skip**: For already booked or waitlisted classes

### 4. Verification System
- Navigates to My Bookings page
- Counts and verifies all bookings
- Compares expected vs actual bookings
- Reports success or mismatch

## Error Handling
- **TimeoutException**: Automatic retry up to 7 times
- **NoSuchElementException**: Graceful handling of missing elements
- **StaleElementReferenceException**: Handled in verification loop

## Output Example
```
Trying login. Attempt: 1
✓ Successfully booked: Yoga on Tuesday
✓ Already booked: Pilates on Thursday
✓ Joined waitlist for: Spinning on Tuesday

--- Total Tuesday/Thursday 6pm classes: 3 ---
--- VERIFYING ON MY BOOKINGS PAGE ---
  ✓ Verified: Yoga
  ✓ Verified: Pilates
  ✓ Verified: Spinning

--- VERIFICATION RESULT ---
Expected: 3 bookings
Found: 3 bookings
✅ SUCCESS: All bookings verified!
```

## Notes
- Remember to manually quit Chrome instance before re-running with `detach=True`
- The script uses explicit waits (2 seconds) for reliability
- Chrome profile persists login sessions
- Network resilience ensures bookings complete even with unstable connections 
