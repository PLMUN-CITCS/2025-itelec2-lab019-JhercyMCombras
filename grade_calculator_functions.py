def get_student_score():

    while True:
        try:

            score = input("Enter the student's score: ")

            score = float(score)

            if score < 0:
                print("Score cannot be negative. Please enter a valid score.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid numerical value for the score.")

def calculate_grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():

    score = get_student_score()

    grade = calculate_grade(score)

    print(f"The student's grade is: {grade}")

if __name__ == "__main__":
    main()
