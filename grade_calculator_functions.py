"""
Grade Calculator Program

This script prompts the user to enter their score, determines their letter grade,
and displays the result. It includes functions for input validation and grading logic.
"""

def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates the input,
    and returns the numerical score as a float.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric score.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.

    Parameters:
    score (float): The student's numerical score.

    Returns:
    str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"  # No need for "else", as return ends function execution

# Main program flow
def main():
    """
    Main function that drives the program.
    It gets the user's score, calculates the grade, and prints the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
