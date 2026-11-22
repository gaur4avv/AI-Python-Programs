"""Generate the Fibonacci sequence using a loop."""


def fibonacci(count: int) -> list[int]:
    """Return the first `count` terms of the Fibonacci sequence."""
    if count < 0:
        raise ValueError("The number of terms cannot be negative.")

    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def main() -> None:
    try:
        count = int(input("Enter the number of Fibonacci terms: "))
        print("Fibonacci sequence:", *fibonacci(count))
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
