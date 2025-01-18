import importlib
import argparse
import os
import sys

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("-day", type=str, required=True, help="Specify the day to run (e.g., '1' for Day 1).")
    args = parser.parse_args()

    # Get the day module
    day_module_name = f"days.day{args.day}"
    try:
        day_module = importlib.import_module(day_module_name)
    except ModuleNotFoundError:
        print(f"Error: Module for Day {args.day} not found.")
        sys.exit(1)

    # Run the solution
    if hasattr(day_module, "solve"):
        day_module.solve()
    else:
        print(f"Error: No 'solve' function in module for Day {args.day}.")

if __name__ == "__main__":
    main()
