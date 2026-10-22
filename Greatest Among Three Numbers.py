def find_greatest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        greatest = find_greatest(num1, num2, num3)
        print(f"The greatest number among {num1}, {num2}, and {num3} is {greatest}.")

    except ValueError:
        print("Please enter valid numbers.")

# Run the main function
if __name__ == "__main__":
    main()