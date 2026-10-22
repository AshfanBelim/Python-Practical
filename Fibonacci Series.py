def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    try:
        terms = int(input("How many terms of the Fibonacci series would you like to display? "))

        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci Series:")
            for i in range(terms):
                print(fibonacci(i), end=' ')
            print()  # for newline
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()