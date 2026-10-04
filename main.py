#temperature converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        c = float(input("Enter temperature in °C: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in °F: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
print("-"*50)
#Student Grade Calculator
def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


def main():
    print("--- Student Grade Calculator ---")
    num_subjects = int(input("Enter the number of subjects: "))

    marks = []
    for i in range(1, num_subjects + 1):
        score = float(input(f"Enter marks for subject {i} (out of 100): "))
        marks.append(score)

    total = sum(marks)
    average = total / num_subjects
    grade = calculate_grade(average)

    print("\n--- Result Summary ---")
    print(f"Total Marks: {total:.2f} / {num_subjects * 100}")
    print(f"Average:     {average:.2f}%")
    print(f"Grade:       {grade}")


if __name__ == "__main__":
    main()
print("-"*50)
#Even/Odd & prime Number checker
import math


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors up to sqrt(n), stepping by 6
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def main():
    print("--- Even/Odd & Prime Checker ---")
    num = int(input("Enter an integer: "))

    # Parity check
    parity = "Even" if is_even(num) else "Odd"
    print(f"{num} is {parity}.")

    # Prime check
    if is_prime(num):
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is NOT a Prime number.")


if __name__ == "__main__":
    main()