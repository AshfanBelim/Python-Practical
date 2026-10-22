def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        number = int(input("Enter a number to find its factorial: "))

        if number <= 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"Factorial of {number} is {factorial(number)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
