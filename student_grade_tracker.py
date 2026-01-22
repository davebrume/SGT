"""
Student Grade Tracker
SDLC Project
"""

# Function to assign letter grade
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)

# Main program
def main():
    students = {}
    print("=== Student Grade Tracker ===")
    
    # Input student data
    num_students = int(input("Enter number of students: "))
    
    for _ in range(num_students):
        name = input("Enter student name: ")
        grades = list(map(int, input(f"Enter grades for {name} (comma separated): ").split(",")))
        avg = calculate_average(grades)
        letter = assign_grade(avg)
        students[name] = {"grades": grades, "average": avg, "letter": letter}
    
    # Display results
    print("\n=== Results ===")
    for name, data in students.items():
        print(f"{name}: Grades={data['grades']}, Average={data['average']:.2f}, Grade={data['letter']}")

if __name__ == "__main__":
    main()
