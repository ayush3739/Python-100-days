# NATO Phonetic Alphabet Converter & List Comprehension

A Python application that converts words into NATO phonetic alphabet code words while demonstrating list and dictionary comprehension concepts.

## Features
- Converts any word to NATO phonetic alphabet
- Uses pandas for efficient CSV data processing
- Dictionary comprehension for fast letter-to-code mapping
- Case-insensitive input handling
- Interactive command-line interface
- Educational list comprehension examples

## How It Works
1. Loads NATO phonetic alphabet data from CSV file
2. Creates a dictionary mapping each letter to its NATO code word
3. Prompts user to enter a word
4. Converts each letter to corresponding NATO phonetic code
5. Displays the complete phonetic representation

## Example Usage
```
Input: "HELLO"
Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

Input: "PYTHON"
Output: ['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

## NATO Phonetic Alphabet Reference
A=Alpha, B=Bravo, C=Charlie, D=Delta, E=Echo, F=Foxtrot, G=Golf, H=Hotel, I=India, J=Juliet, K=Kilo, L=Lima, M=Mike, N=November, O=Oscar, P=Papa, Q=Quebec, R=Romeo, S=Sierra, T=Tango, U=Uniform, V=Victor, W=Whiskey, X=X-ray, Y=Yankee, Z=Zulu

## Files
- `main.py` - Main phonetic alphabet converter
- `nato_phonetic_alphabet.csv` - NATO alphabet data (A-Z with code words)
- `list or dictionary comrehension.ipynb` - Learning notebook for comprehension concepts

## Learning Concepts
- List comprehension syntax and usage
- Dictionary comprehension techniques
- Pandas CSV file processing
- String manipulation and iteration
- Data structure transformations
- Functional programming concepts

## Technical Implementation
- Dictionary comprehension: `{row.letter:row.code for (index, row) in data.iterrows()}`
- List comprehension: `[new_dict[letter] for letter in user_input]`
- Pandas iterrows() method for DataFrame iteration
- String upper() method for input normalization

## Requirements
- Python 3.x
- pandas library

## Installation
```bash
pip install pandas
python main.py
```

## Educational Value
Perfect for learning:
- Advanced Python comprehension syntax
- Data processing with pandas
- Real-world application of NATO standards
- Efficient dictionary and list operations

Great for radio operators, pilots, or anyone learning Python comprehensions!