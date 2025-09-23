# Turtle Crossing Game

A classic Frogger-style arcade game built with Python's turtle graphics where a turtle tries to cross a busy road while avoiding oncoming cars.

## Features
- **Player Movement**: Control turtle with arrow keys to move forward
- **Dynamic Car Spawning**: Random car generation with varied colors and positions  
- **Collision Detection**: Game ends when turtle hits a car
- **Progressive Difficulty**: Cars move faster as levels increase
- **Level Tracking**: Visual scoreboard showing current level
- **Finish Line Detection**: Advance levels by reaching the top of the screen

## How It Works
1. Player controls a turtle starting at the bottom of the screen
2. Cars spawn randomly from the right side and move left across the screen
3. Player must navigate through traffic to reach the finish line at the top
4. Each successful crossing increases the level and car speed
5. Game ends when the turtle collides with a car

## Game Controls
- **Up Arrow**: Move turtle forward
- **Click Screen**: Exit game when finished

## Example Gameplay
- Start at Level 1 with slow-moving cars
- Navigate turtle safely across the road
- Reach the top to advance to Level 2 with faster cars
- Continue advancing levels for increasing challenge
- Avoid collision to maintain your progress

## Files
- `main.py` - Main game loop, collision detection, and game state management
- `player.py` - Player turtle class with movement and boundary checking
- `car_manager.py` - Car spawning, movement, and speed management system
- `scoreboard.py` - Level display and game over screen functionality

## Learning Concepts
- **Object-Oriented Programming**: Multiple classes with inheritance
- **Game Loop Architecture**: Continuous update cycle with event handling
- **Collision Detection**: Distance-based collision algorithms
- **Random Generation**: Probabilistic car spawning and positioning
- **State Management**: Game state tracking and level progression
- **Event-Driven Programming**: Keyboard input handling
- **Graphics Programming**: Turtle graphics for game visuals

## Technical Implementation
- **Turtle Graphics**: Built using Python's built-in turtle module
- **Object Classes**: Player, CarManager, and Scoreboard classes
- **Collision Algorithm**: Distance calculation between turtle and cars
- **Speed Scaling**: Progressive difficulty through speed increments
- **Screen Management**: 600x600 pixel game window with coordinate system

## Requirements
- Python 3.x
- tkinter (usually included with Python)
- turtle module (built-in)

## Installation
```bash
python main.py
```

## Game Constants
- **Player Speed**: 10 pixels per move
- **Initial Car Speed**: 5 pixels per frame
- **Speed Increment**: +5 pixels per level
- **Collision Distance**: 20 pixels
- **Car Spawn Probability**: 1 in 6 chance per frame

## Educational Value
Perfect for learning:
- Game development fundamentals
- Object-oriented design patterns
- Real-time collision detection
- Progressive difficulty systems
- Event-driven user interfaces
- Coordinate geometry in programming

Great introduction to game programming concepts while building an engaging arcade-style experience!