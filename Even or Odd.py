def is_even(num):
    return num % 2 == 0

def main():
    try:
        number = int(input("Enter a number: "))

        if is_even(number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()