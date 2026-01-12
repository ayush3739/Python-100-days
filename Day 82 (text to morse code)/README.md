# Text to Morse Code Converter

A command-line Python program that converts text input into Morse code. This project demonstrates string manipulation, dictionary lookups, error handling, and input validation in a practical utility application.

## Features

- **Complete Character Support**: Letters A-Z, numbers 0-9, space, and common punctuation
- **Input Validation**: Detects unsupported characters and provides helpful error messages
- **Case Insensitive**: Automatically converts input to uppercase
- **Whitespace Handling**: Properly handles multiple spaces and empty input
- **Clear Output**: Easy-to-read Morse code with proper spacing
- **Error Handling**: Graceful handling of invalid input
- **Interactive CLI**: Simple command-line interface

## How to Use

1. Run the program:
   ```bash
   python main.py
   ```

2. Enter your text when prompted:
   ```
   Enter the text you want to convert to the morse code : Hello World
   ```

3. Receive Morse code output:
   ```
   The morse code is : .... . .-.. .-.. --- / .-- --- .-. .-.. -..
   ```

4. Run again with different input to test various scenarios

## Supported Characters

### Letters (A-Z)
All uppercase and lowercase letters are supported:
```
A: .-      B: -...    C: -.-.    D: -..
E: .       F: ..-.    G: --.     H: ....
I: ..      J: .---    K: -.-     L: .-..
M: --      N: -.      O: ---     P: .--.
Q: --.-    R: .-.     S: ...     T: -
U: ..-     V: ...-    W: .--     X: -..-
Y: -.--    Z: --..
```

### Numbers (0-9)
```
0: -----   1: .----   2: ..---   3: ...--   4: ....-
5: .....   6: -....   7: --...   8: ---..   9: ----.
```

### Punctuation
```
. (period): .-.-.-       , (comma): --..--
? (question): ..--..     ! (exclamation): -.-.--
: (colon): ---...        ; (semicolon): -.-.-.
( (parenthesis): -.--.-  ) (parenthesis): -.--.-
" (quote): .-..-.        ' (apostrophe): .----.
@ (at): .--.-.           / (slash): -..-.
- (hyphen): -....-       = (equals): -...-
```

### Special
- **Space**: Converted to `/` in Morse code
- Separates words in output

## Technical Details

### Morse Code Dictionary
The program uses a Python dictionary to map characters to their Morse equivalents:
```python
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', ...
    '0': '-----', '1': '.----', ...
    '.': '.-.-.-', ',': '--..--', ...
    ' ': '/'
}
```

### Conversion Algorithm
1. **Input Acquisition**: Get text from user via `input()`
2. **Preprocessing**:
   - Convert to uppercase (`.upper()`)
   - Split into words (`.split(' ')`)
   - Remove empty strings from list
   - Rejoin with single spaces
3. **Validation**: Check for empty input after cleaning
4. **Conversion Loop**:
   - Iterate through each character
   - Look up character in dictionary
   - If found: append Morse code + space
   - If not found: return error message
5. **Output**: Display converted Morse code (remove trailing space)

### Error Handling

**Empty Input**:
```python
if len(sentence)==0:
    return "Error: Empty input. Please enter text to convert."
```

**Unsupported Character**:
```python
if i not in morse_code:
    return f"Error: Unsupported character {i} found"
```

**Input Processing**:
- Handles multiple consecutive spaces
- Filters out empty strings
- Validates before conversion

## File Structure

```
Day 82 (text to morse code)/
└── main.py           # Main program with converter function
```

## Code Breakdown

### Main Components

**1. Morse Code Dictionary**:
- Complete mapping of characters to Morse code
- Includes letters, numbers, punctuation
- Space character maps to `/`

**2. `text_to_morse()` Function**:
- **Parameters**: `sentence` (string to convert)
- **Returns**: Converted Morse code or error message
- **Process**: Clean, validate, convert, format output

**3. Main Execution**:
- Get user input
- Call conversion function
- Display result

### Example Usage

**Input**: `Hello World`
**Process**:
```
H -> ....
E -> .
L -> .-..
L -> .-..
O -> ---
  -> /
W -> .--
O -> ---
R -> .-.
L -> .-..
D -> -..
```
**Output**: `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

## Learning Concepts

### Python Fundamentals
- Dictionary data structures
- String manipulation methods
- List comprehensions
- Conditional logic
- Loop iteration
- Function definition and return values

### String Operations
- `.upper()` - Convert to uppercase
- `.split()` - Split string into list
- `.join()` - Combine list into string
- String slicing `[:-1]` - Remove last character
- String concatenation with `+=`

### Data Structures
- Dictionary lookups with `in` operator
- List filtering and comprehension
- String building and formatting

### Input/Output
- `input()` function for user interaction
- `print()` for output display
- F-strings for formatted error messages

### Error Handling
- Input validation
- Early return patterns
- Descriptive error messages
- Edge case handling

## Requirements

- Python 3.x (no external libraries needed)
- Command-line terminal

## Environment Setup

### Windows (PowerShell):
```bash
py main.py
```

### macOS/Linux:
```bash
python3 main.py
```

## How the Code Works

1. **Dictionary Definition**: Creates complete Morse code mapping
2. **Function Definition**: Defines `text_to_morse()` with conversion logic
3. **User Input**: Prompts for text to convert
4. **Preprocessing**: Cleans and validates input string
5. **Empty Check**: Returns error if no valid characters
6. **Character Loop**: Iterates through each character:
   - Checks if character exists in dictionary
   - Appends Morse code or returns error
7. **Output Formatting**: Removes trailing space and returns result
8. **Display**: Prints final Morse code to console

## Practical Applications

### Educational
- Learning Morse code
- Understanding encoding systems
- Teaching programming concepts
- String manipulation practice

### Communication
- Emergency signaling
- Amateur radio practice
- Historical communication methods
- Accessibility tools

### Cryptography
- Basic encoding demonstration
- Cipher understanding
- Character mapping concepts
- Translation systems

## Testing Examples

**Valid Input**:
```
Input: "SOS"
Output: "... --- ..."

Input: "Python 3.9"
Output: ".--. -.-- - .... --- -. / ...-- .-.-.- ----.."

Input: "Hello, World!"
Output: ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
```

**Error Cases**:
```
Input: ""
Output: "Error: Empty input. Please enter text to convert."

Input: "Hello 😊"
Output: "Error: Unsupported character 😊 found"
```

## Next Steps/Improvements

- Add Morse code to text decoder
- Implement audio output (beep patterns)
- Create visual output (light flashing)
- Add GUI interface
- Support file input/output
- Create web version
- Add international Morse codes
- Implement timing standards
- Add batch conversion
- Create API endpoint
- Add clipboard integration
- Support custom character mappings
- Add prosigns (KN, SK, etc.)
- Implement real-time conversion
- Add educational mode with hints

Perfect for learning string manipulation, dictionary operations, input validation, and building practical text processing utilities!
