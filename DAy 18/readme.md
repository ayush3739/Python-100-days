# Turtle Graphics Art - Hirst Painting

A colorful dot painting generator inspired by Damien Hirst's spot paintings, created using Python's Turtle graphics.

## Features
- Generates a 10x10 grid of colored dots
- Uses extracted color palette from real artwork
- Random color selection for each dot
- Turtle graphics animation
- Click to exit functionality

## How It Works
1. Uses a predefined color palette extracted from actual artwork
2. Turtle moves in a grid pattern
3. Creates 100 dots total (10 rows × 10 columns)
4. Each dot is randomly colored from the palette
5. Positions are calculated automatically for perfect spacing

## Color Palette
The program uses 30 carefully selected colors extracted from real artwork:
- Earth tones and pastels
- Vibrant primary colors
- Subtle background shades

## Files
- `main.py` - Main dot painting generator
- `learn turtle.ipynb` - Jupyter notebook for learning turtle graphics
- `image.jpg` - Reference image (if used for color extraction)

## Technical Details
- Dot size: 20 pixels
- Spacing: 50 pixels between dots
- Grid: 10×10 pattern
- Total dots: 100
- Speed: Fastest turtle speed for quick generation

## Requirements
- Python 3.x
- turtle module (included with Python)
- colorgram.py (for color extraction - optional)

## Usage
```bash
python main.py
```

## Learning Concepts
- Turtle graphics and positioning
- Color management and RGB values
- Loop structures and positioning logic
- Random selection algorithms
- Grid-based drawing patterns

**Note**: This code demonstrates color extraction concepts but works with a predefined palette for compatibility.