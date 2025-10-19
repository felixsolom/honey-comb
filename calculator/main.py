import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def evaluate_expression(calculator, expression):
    """Evaluates the given expression using the calculator.

    Args:
        calculator: The Calculator instance to use.
        expression: The expression to evaluate.

    Returns:
        The result of the evaluation, or None if an error occurs.
    """
    try:
        if not expression or expression.strip() == "":
            print("Error: Expression is empty or contains only whitespace.")
            return None
        result = calculator.evaluate(expression)
        return result
    except ZeroDivisionError as e:
        print(f"Error: Division by zero: {e}")
        return None
    except SyntaxError as e:
        print(f"Error: Invalid syntax: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to run the calculator application."""
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    result = evaluate_expression(calculator, expression)

    if result is not None:
        to_print = format_json_output(expression, result)
        print(to_print)


if __name__ == "__main__":
    main()