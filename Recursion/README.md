# Recursion Calculator

A beautiful GUI application for calculating Factorial, Permutation, and Combination values using optimized recursive algorithms.

## Features

- Modern, dark-themed user interface
- Memory-efficient recursive calculations using memoization
- Support for large numbers
- Real-time operation switching
- Error handling and input validation
- Responsive design

## Operations

1. **Factorial (n!)**: Calculates the product of all positive integers less than or equal to n
2. **Permutation (P(n,r))**: Calculates the number of ways to arrange r items from a set of n items
3. **Combination (C(n,r))**: Calculates the number of ways to select r items from a set of n items

## Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python calculator.py
   ```

## Implementation Details

- Uses `@lru_cache` for memoization to optimize recursive calculations
- Built with CustomTkinter for a modern UI experience
- Implements error handling for invalid inputs and large numbers
- Uses grid layout manager for responsive design

## Requirements

- Python 3.7+
- customtkinter
- pillow

## Note

For very large numbers, the calculation might take longer or may not be possible due to Python's recursion depth limit and memory constraints.
