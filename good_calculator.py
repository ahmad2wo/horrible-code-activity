"""
GOOD CODE VERSION (clean + best practices)
Goal: A simple CLI calculator that follows best practices.
Run: python good_calculator.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Tuple


# Principles demonstrated:
# 1) DRY: one shared flow; operations stored in a map, no copy/paste branches
# 2) Single Responsibility: input parsing, calculation, and UI are separate
# 3) Separation of Concerns: pure functions do math; CLI handles user interaction


@dataclass(frozen=True)
class Operation:
    """Represents one calculator operation shown in the menu."""
    key: str
    name: str
    func: Callable[[float, float], float]


def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a / b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def average(a: float, b: float) -> float:
    """Return the average of a and b."""
    return (a + b) / 2


def build_operations() -> Dict[str, Operation]:
    """Create the menu operations in one place (DRY)."""
    ops = [
        Operation("1", "Add", add),
        Operation("2", "Subtract", subtract),
        Operation("3", "Multiply", multiply),
        Operation("4", "Divide", divide),
        Operation("5", "Power", power),
        Operation("6", "Average", average),
    ]
    return {op.key: op for op in ops}


def prompt_float(prompt: str) -> float:
    """Prompt the user for a float with validation."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number (example: 3, 3.14, -2).")


def print_menu(ops: Dict[str, Operation]) -> None:
    """Display the calculator menu."""
    print("\n=== Clean Calculator ===")
    for key in sorted(ops.keys()):
        print(f"{key}) {ops[key].name}")
    print("7) Quit")


def run_calculator() -> None:
    """Main loop for the CLI calculator (UI layer)."""
    ops = build_operations()

    while True:
        print_menu(ops)
        choice = input("Choose an option: ").strip()

        if choice == "7":
            print("Goodbye!")
            return

        op = ops.get(choice)
        if not op:
            print("Invalid choice. Please pick a menu number.")
            continue

        a = prompt_float("Number 1: ")
        b = prompt_float("Number 2: ")

        try:
            result = op.func(a, b)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        print(f"Result ({op.name}): {result}")


def main() -> None:
    run_calculator()


if __name__ == "__main__":
    main()
