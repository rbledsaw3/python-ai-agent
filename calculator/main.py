import sys
from pkg.calculator import Calculator
from pkg.render import render

def print_usage():
    usage = """
        Calculator App
Usage: python3 main.py "<EXPRESSION>"
Example: python3 main.py "3 + 5"
"""
    print(usage)

def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print_usage()
        sys.exit(1)

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exeception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
