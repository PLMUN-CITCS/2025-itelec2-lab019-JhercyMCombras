def get_student_score() -> float:
    """
    Prompts the user to enter their score and returns it as a numerical value.
    
    Returns:
        float: The score entered by the user.
    """
    while True:
        try:
            # Get user input and convert it to float for flexibility
            score = float(input("Enter your score: "))
            
            # Check if the score is within a valid range
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score using conditional statements.
    
    Parameters:
        score (float): The numerical score to determine the grade.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
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

# Main Program Flow
if __name__ == "__main__":
    # Get the student's score
    score = get_student_score()
    
    # Calculate the grade
    grade = calculate_grade(score)
    
    # Display the result
    print(f"Your Grade is: {grade}")
