# Coffee Machine - Object-Oriented Programming

An enhanced coffee machine simulator built using Object-Oriented Programming principles, refactoring the procedural version into modular classes.

## Features
- **Object-Oriented Design**: Separate classes for different responsibilities
- **Modular Architecture**: Clean separation of concerns
- **Resource Management**: Coffee maker handles ingredients and operations
- **Money Handling**: Dedicated money machine for payment processing
- **Menu System**: Organized menu structure with item management
- **Type Safety**: Proper class structure and method organization

## Class Structure
- **CoffeeMaker**: Manages resources (water, milk, coffee) and brewing operations
- **MoneyMachine**: Handles payment processing, change calculation, and profit tracking
- **Menu**: Manages available drinks and their specifications
- **MenuItem**: Individual drink specifications and requirements

## How It Works
1. Menu displays available options and prices
2. Customer selects a drink
3. Coffee maker checks resource availability
4. Money machine processes payment
5. If successful, coffee maker brews the drink
6. Resources are updated automatically

## OOP Benefits Demonstrated
- **Encapsulation**: Data and methods grouped in relevant classes
- **Modularity**: Easy to maintain and extend functionality
- **Reusability**: Classes can be imported and used in other projects
- **Clarity**: Clear responsibility separation

## Files
- `main.py` - Main program orchestrating the objects
- `coffee_maker.py` - CoffeeMaker class for brewing and resource management
- `money_machine.py` - MoneyMachine class for payment processing
- `menu.py` - Menu and MenuItem classes for menu management
- `learn oop.ipynb` - Learning notebook for OOP concepts

## Learning Concepts
- Object-Oriented Programming fundamentals
- Class creation and instantiation
- Method definition and calling
- Data encapsulation and abstraction
- Modular code organization
- Class interaction and communication

## Requirements
- Python 3.x
- Basic understanding of OOP concepts

## Usage
```bash
python main.py
```

## Comparison with Procedural Version
This OOP version (Day 16) improves upon the procedural version (Day 15) by:
- Better code organization
- Easier maintenance and debugging
- Reusable components
- Clear separation of responsibilities
- More professional code structure

Perfect for learning OOP fundamentals while building a practical application!