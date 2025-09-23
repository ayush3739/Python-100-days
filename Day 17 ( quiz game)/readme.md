# Quiz Game - Object-Oriented Programming

A trivia quiz game built using Object-Oriented Programming principles with True/False questions.

## Features
- Object-oriented design with separate classes
- True/False trivia questions
- Score tracking throughout the game
- Question bank management
- Interactive command-line interface
- Final score reporting

## How It Works
1. Questions are loaded from the question bank
2. Each question is presented one at a time
3. User provides True/False answers
4. Score is updated for correct answers
5. Game continues until all questions are answered
6. Final score and completion message displayed

## Class Structure
- **Question**: Represents individual trivia questions
- **QuizBrain**: Manages game logic, scoring, and question flow
- **Data Module**: Contains question data from API

## Files
- `main.py` - Main game orchestration and setup
- `question_model.py` - Question class definition
- `quiz_brain.py` - Quiz game logic and brain
- `data.py` - Question database/API data
- `creating class.ipynb` - Learning notebook for OOP concepts

## Question Format
Questions are sourced from trivia APIs and include:
- Question text
- Correct answer (True/False)
- Category information
- Difficulty level

## Learning Concepts
- Object-Oriented Programming (OOP)
- Class creation and instantiation
- Method definition and calling
- Data encapsulation
- List comprehension
- API data processing

## Requirements
- Python 3.x
- Basic understanding of OOP concepts

## Usage
```bash
python main.py
```

## Game Flow
1. Question bank is populated from data source
2. Quiz brain is initialized with questions
3. Questions are presented sequentially
4. User input is processed and validated
5. Score tracking continues throughout
6. Game ends with final score display

Perfect for learning OOP fundamentals while building an engaging quiz application!