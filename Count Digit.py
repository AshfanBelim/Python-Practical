def count_characters(s):
    letters = 0
    digits = 0
    others = 0

    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else:
            others += 1

    return letters, digits, others

def main():
    input_string = input("Enter a string: ")

    letters, digits, others = count_characters(input_string)

    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    print(f"Other Characters: {others}")

# Run the main function
if __name__ == "__main__":
    main()
