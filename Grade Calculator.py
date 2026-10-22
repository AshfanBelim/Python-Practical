def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average > 90:
        return 'A'
    elif 80 <= average <= 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    else:
        return 'Fail'

def main():
    try:
        marks = []
        for i in range(5):
            subject_marks = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(subject_marks)

        grade = calculate_grade(marks)
        print(f"Average Marks: {sum(marks) / 5}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Please enter valid marks as numbers.")

# Run the main function
if __name__ == "__main__":
    main()
