# Flash Card App (Updated Version)

An enhanced flash card language learning application with improved error handling and data persistence.

## Features
- **French-English Vocabulary Learning**: Complete flash card system
- **Smart Data Management**: Tracks learning progress automatically
- **Error Handling**: Robust exception handling for missing files
- **Auto-Save Progress**: Saves words you still need to learn
- **Visual Flash Cards**: Card flip animation and intuitive interface
- **Adaptive Learning**: Focuses on words you haven't mastered

## How the App Works
1. **Initial Load**: Tries to load your existing progress file
2. **Fallback System**: If no progress exists, loads the complete word database
3. **Study Session**: Shows French words with automatic English translation reveal
4. **Progress Tracking**: Mark words as known/unknown
5. **Smart Filtering**: Removes known words from future sessions
6. **Auto-Save**: Saves your learning progress after each session

## Directory Structure
- `main.py` - Enhanced flash card application
- `data/` - Data directory containing:
  - `french_words.csv` - Complete vocabulary database
  - `words_to_learn.csv` - Your personalized learning list
- `images/` - Image assets for the interface

## Learning Algorithm
1. **Load Progress**: Check for existing `words_to_learn.csv`
2. **Exception Handling**: Fall back to `french_words.csv` if needed
3. **Study Loop**: Present cards with timing mechanism
4. **User Feedback**: Process known/unknown selections
5. **Data Update**: Remove mastered words from study deck
6. **Progress Save**: Write updated word list to CSV

## Error Handling Features
- **File Not Found**: Gracefully handles missing progress files
- **Data Corruption**: Falls back to original dataset if needed
- **CSV Processing**: Robust pandas error handling
- **State Recovery**: Always ensures app can start successfully

## Technical Implementation
```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

## Learning Concepts
- **Exception Handling**: Try/except blocks for robust error management
- **Data Persistence**: CSV file management with pandas
- **GUI Development**: Advanced Tkinter interface design
- **State Management**: Maintaining application state across sessions
- **File I/O**: Reading and writing structured data
- **User Experience**: Smooth error recovery and data handling

## Requirements
- Python 3.x
- pandas
- tkinter (included with Python)

## Usage
```bash
python main.py
```

## Progress Tracking
- **First Run**: Uses complete french_words.csv database
- **Subsequent Runs**: Loads your personalized words_to_learn.csv
- **Adaptive Learning**: Deck shrinks as you master vocabulary
- **Never Lose Progress**: Automatic saving after each session

## File Management
- Creates `words_to_learn.csv` automatically
- Maintains synchronized data between sessions
- Handles missing files gracefully
- Preserves learning progress indefinitely

Perfect for learning exception handling and data persistence while building a practical language learning tool!