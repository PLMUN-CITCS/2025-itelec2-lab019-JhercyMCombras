def get_student_score():
   
    while True:
        try:
            score = float(input("Enter the student's score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


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


def display_grade(grade):

    print(f"The student's grade is: {grade}")


def main():

    score = get_student_score()
    grade = calculate_grade(score)
    display_grade(grade)


if __name__ == "__main__":
    main()