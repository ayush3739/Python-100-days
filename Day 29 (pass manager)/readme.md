# Password Manager

A secure password management application with GUI interface for storing and generating strong passwords.

## Features
- **Password Generation**: Creates strong, random passwords
- **Secure Storage**: Saves passwords with website and email info
- **Password Copy**: Automatically copies generated passwords to clipboard
- **User-Friendly GUI**: Clean Tkinter interface with logo
- **Input Validation**: Prevents saving empty fields
- **Confirmation Dialog**: Confirms before saving passwords

## How It Works
1. Enter website name and email/username
2. Generate a secure password or enter your own
3. Review the details in confirmation dialog
4. Save to password database
5. Password is automatically copied to clipboard

## Password Generation
- **8-10 letters** (mixed case)
- **2-4 numbers**
- **2-4 special characters**
- **Shuffled randomly** for maximum security
- **Auto-copied** to clipboard for convenience

## Security Features
- Random password generation using Python's random module
- Mixed character types for strong passwords
- Immediate clipboard copy for secure pasting
- Local file storage (extend to encrypted storage)

## Files
- `main.py` - Main password manager application
- `logo.png` - Application logo
- `password generator.py` - Standalone password generator
- `demo.txt` - Sample data file

## GUI Components
- Website entry field
- Email/Username entry field
- Password entry field with generate button
- Add button to save passwords
- Logo display
- Input validation and dialogs

## Usage
```bash
python main.py
```

## Password Generator Features
- Customizable password length
- Multiple character sets (letters, numbers, symbols)
- Cryptographically secure randomization
- Instant clipboard integration

## Security Considerations
- Passwords stored in plain text (demo version)
- Consider encryption for production use
- Secure master password implementation recommended
- Regular backup of password database

## Learning Concepts
- GUI development with Tkinter
- File I/O operations
- Random password generation algorithms
- Clipboard integration
- Input validation
- User experience design
- Security best practices

## Requirements
- Python 3.x
- tkinter (included with Python)
- pyperclip (for clipboard functionality)

## Installation
```bash
pip install pyperclip
python main.py
```

## Customization
- Modify password generation rules
- Add encryption for stored passwords
- Implement search functionality
- Add password strength indicators
- Include password expiry tracking

Perfect for learning GUI development while building a practical security tool!