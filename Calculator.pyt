import math


def add(*args):
    return sum(args)


def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num != 0:
            result /= num
        else:
            raise ValueError("Number can't be divided by zero!")
    return result


def power(*args):
    result = args[0]
    for num in args[1:]:
        if num != 0:
            result = power(num)
        else:
            raise ValueError("number can't be raised to any number")


def calculator():
    print("simple calculator")
    print("1. add")
    print("2. substraction")
    print("3. multiplication")
    print("4. divide")
    print("5. exponent")

    choice = int(input("Enter numbers to calculate them! "))

    if choice == 1:
        nums = list(
            map(float, input("Enter numbers to add separated by space: ").split()))
        print("Result:", add(*nums))
    elif choice == 2:
        nums = list(
            map(float, input("Enter numbers to subtract separated by space: ").split()))
        print("Result:", subtract(*nums))
    elif choice == 3:
        nums = list(
            map(float, input("Enter numbers to multiply separated by space: ").split()))
        print("Result:", multiply(*nums))
    elif choice == 4:
        nums = list(
            map(float, input("Enter numbers to divide separated by space: ").split()))
    elif choice == 5:
        nums = list(
            map(float, input("Enter numbers to its power separated by space: ").split()))
        try:
            print("Result:", divide(*nums))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    calculator()
