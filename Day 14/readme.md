# Higher or Lower Game

A guessing game where players compare follower counts of famous celebrities, influencers, and public figures.

## Features
- Random celebrity/influencer selection
- Interactive comparison gameplay
- Score tracking system
- Clear screen between rounds
- Continuous play until wrong guess
- Celebrity information display

## How to Play
1. Two celebrities are presented (A and B)
2. Choose who has more followers by typing 'A' or 'B'
3. Correct guesses increase your score
4. Game continues until you make a wrong choice
5. Final score is displayed when you lose

## Game Mechanics
- Celebrities are randomly selected from a database
- No duplicate comparisons in consecutive rounds
- Winner becomes the next comparison candidate
- Score accumulates with each correct answer

## Files
- `higher or lower.py` - Main game logic
- `data.py` - Celebrity database with follower counts
- `images.py` - ASCII art for logo and VS graphics

## Celebrity Database
Includes various public figures with:
- Name and description
- Country of origin
- Follower count data
- Categories: actors, musicians, athletes, influencers, etc.

## Game Features
- Clear console between rounds
- ASCII art graphics
- Cross-platform screen clearing
- Input validation
- Score persistence during game session

## Requirements
- Python 3.x
- Standard library modules (random, os)

## Usage
```bash
python "higher or lower.py"
```

## Learning Concepts
- Random selection algorithms
- Data structure management
- User input handling
- Game loop implementation
- Cross-platform compatibility
- Modular code organization

Test your knowledge of social media influence and see how high you can score!