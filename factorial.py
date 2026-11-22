"""Calculate the factorial of a non-negative integer using recursion."""


def factorial(number: int) -> int:
    """Return number! using a recursive function."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def main() -> None:
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"{number}! = {factorial(number)}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
