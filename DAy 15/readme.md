# Coffee Machine

A command-line coffee machine simulator that processes orders, manages resources, and handles payments.

## Features
- Multiple coffee options (Espresso, Latte, Cappuccino)
- Resource management (water, milk, coffee, money)
- Payment processing with coin insertion
- Resource checking before making drinks
- Administrative report generation
- Automatic change calculation

## How It Works
1. User selects a drink from the menu
2. System checks if enough resources are available
3. User inserts coins for payment
4. System validates payment amount
5. If sufficient payment, drink is prepared and resources are deducted
6. Change is returned if overpaid

## Available Commands
- `espresso` - Order an espresso (₹1.5)
- `latte` - Order a latte (₹2.5)
- `cappuccino` - Order a cappuccino (₹3.0)
- `report` - Display current resource levels
- `off` - Turn off the machine

## Resource Requirements
- **Espresso**: 50ml water, 18g coffee
- **Latte**: 200ml water, 150ml milk, 24g coffee
- **Cappuccino**: 250ml water, 100ml milk, 24g coffee

## Files
- `coffee machine .py` - Main coffee machine program

## Requirements
- Python 3.x

## Usage
```bash
python "coffee machine .py"
```

Perfect for learning about resource management, user input validation, and basic business logic implementation!