"""
Student Academic Performance Analysis System
GSE301 Data Science: Python Fundamentals

This system stores, processes, and analyzes academic data for students.
"""


# ============================================================================
# PART 1: DATA COLLECTION AND STORAGE
# ============================================================================

# Task 1.1: Variable Declaration and Data Types
# Sample student data structure
student_name = "Rasheed Fatia"
matric_number = "23/60AC389"
age = 22
cgpa = 4.81
is_active = True
courses_registered = ["ELE567", "Data Science", "Statistics"]
grades = {"Python": "A", "Statistics": "A", "Data Science": "A"}

# Task 1.2: Data Structures in Action
# List of student names
student_names = [
    "Rasheed Fatia",
    "Yusuf Adeoye",
    "Moses Oyedele",
    "Timi Abidoye",
    "Nimah Nina"
]

# Dictionary for each student's full profile
students_data = {
    "Rasheed Fatia": {
        "matric": "23/60AC389",
        "age": 22,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["ELE567", "Data Science", "Statistics"],
        "grades": {"Python": "A", "Statistics": "A", "Data Science": "A"},
        "scores": {"Python": 95, "Statistics": 92, "Data Science": 88}
    },
    "Yusuf Adeoye": {
        "matric": "23/70JC093",
        "age": 21,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Algorithms", "Networking"],
        "grades": {"Python": "B", "Algorithms": "B", "Networking": "C"},
        "scores": {"Python": 75, "Algorithms": 78, "Networking": 65}
    },
    "Moses Oyedele": {
        "matric": "23/50AB123",
        "age": 23,
        "cgpa": 3.20,
        "is_active": True,
        "courses": ["Python", "Statistics", "Database"],
        "grades": {"Python": "C", "Statistics": "B", "Database": "C"},
        "scores": {"Python": 68, "Statistics": 75, "Database": 70}
    },
    "Timi Abidoye": {
        "matric": "23/40CD456",
        "age": 20,
        "cgpa": 4.50,
        "is_active": True,
        "courses": ["Python", "Data Science", "Machine Learning"],
        "grades": {"Python": "A", "Data Science": "A", "Machine Learning": "B"},
        "scores": {"Python": 90, "Data Science": 88, "Machine Learning": 82}
    },
    "Nimah Nina": {
        "matric": "23/30EF789",
        "age": 22,
        "cgpa": 2.80,
        "is_active": False,
        "courses": ["Python", "Statistics"],
        "grades": {"Python": "D", "Statistics": "C"},
        "scores": {"Python": 55, "Statistics": 65}
    }
}

# Set to store unique courses offered in the department
unique_courses = {
    "Python", "Statistics", "Data Science", "Algorithms",
    "Networking", "Database", "Machine Learning", "ELE567"
}

# Tuple for fixed department information
department_info = ("Religion department", "Faculty of Technology", 2025)


# ============================================================================
# PART 2: DATA PROCESSING AND LOGIC
# ============================================================================

def get_grade(score):
    """
    Task 2.1: Conditional Statements for Grading
    Accepts a score from 0 to 100 and returns a grade using IF, ELIF, ELSE
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"


def get_grade_feedback(grade):
    """
    Task 2.1: Uses MATCH CASE to print feedback based on the grade
    """
    match grade:
        case "A":
            return "Excellent! Outstanding performance."
        case "B":
            return "Very good! Keep up the great work."
        case "C":
            return "Good performance. Room for improvement."
        case "D":
            return "Fair performance. Consider seeking help."
        case "E":
            return "Below average. Extra effort needed."
        case "F":
            return "Failed. Please retake the course."
        case _:
            return "Invalid grade."


def validate_user_input():
    """
    Task 2.2: Type Conversion and Validation
    Ask the user to input age and CGPA as strings
    Convert them to int and float
    Validate age between 16 and 40, and CGPA between 0.0 and 5.0
    Use TRY EXCEPT to handle invalid input
    """
    print("\n--- Input Validation Example ---")
    
    # Get age input
    while True:
        try:
            age_str = input("Enter age (as string): ")
            age_int = int(age_str)
            
            if 16 <= age_int <= 40:
                print(f"✓ Valid age: {age_int}")
                break
            else:
                print("✗ Age must be between 16 and 40. Please try again.")
        except ValueError:
            print("✗ Invalid input! Please enter a valid integer.")
    
    # Get CGPA input
    while True:
        try:
            cgpa_str = input("Enter CGPA (as string): ")
            cgpa_float = float(cgpa_str)
            
            if 0.0 <= cgpa_float <= 5.0:
                print(f"✓ Valid CGPA: {cgpa_float}")
                break
            else:
                print("✗ CGPA must be between 0.0 and 5.0. Please try again.")
        except ValueError:
            print("✗ Invalid input! Please enter a valid number.")
    
    return age_int, cgpa_float


# ============================================================================
# PART 3: ANALYSIS AND REPORTING
# ============================================================================

def demonstrate_list_operations():
    """
    Task 3.1: List Operations and Slicing
    Given a list of 10 assignment scores:
    - Extract the top 3 scores using slicing
    - Extract the last 5 scores using negative indexing
    - Extract every other score using step slicing
    """
    assignment_scores = [85, 92, 78, 95, 88, 90, 82, 87, 91, 79]
    
    print("\n--- List Operations Demonstration ---")
    print(f"Original scores: {assignment_scores}")
    
    # Extract top 3 scores (first 3)
    top_3 = assignment_scores[:3]
    print(f"Top 3 scores: {top_3}")
    
    # Extract last 5 scores using negative indexing
    last_5 = assignment_scores[-5:]
    print(f"Last 5 scores: {last_5}")
    
    # Extract every other score using step slicing
    every_other = assignment_scores[::2]
    print(f"Every other score: {every_other}")
    
    return assignment_scores


def demonstrate_set_operations():
    """
    Task 3.2: Set Operations
    Given two sets:
    - set_pass: students who passed Python
    - set_merit: students with CGPA above 4.0
    Find:
    - Students who passed and have merit (intersection)
    - All distinct students in both sets (union)
    - Students who passed but do not have merit (difference)
    """
    # Students who passed Python (score >= 50)
    set_pass = set()
    for name, data in students_data.items():
        if "Python" in data.get("scores", {}) and data["scores"]["Python"] >= 50:
            set_pass.add(name)
    
    # Students with CGPA above 4.0
    set_merit = set()
    for name, data in students_data.items():
        if data["cgpa"] > 4.0:
            set_merit.add(name)
    
    print("\n--- Set Operations Demonstration ---")
    print(f"Students who passed Python: {set_pass}")
    print(f"Students with CGPA > 4.0: {set_merit}")
    
    # Intersection: students who passed AND have merit
    intersection = set_pass & set_merit
    print(f"Passed AND have merit (intersection): {intersection}")
    
    # Union: all distinct students in both sets
    union = set_pass | set_merit
    print(f"All students in both sets (union): {union}")
    
    # Difference: passed but do not have merit
    difference = set_pass - set_merit
    print(f"Passed but no merit (difference): {difference}")
    
    return set_pass, set_merit


# ============================================================================
# PART 4: INTERACTIVE MENU SYSTEM
# ============================================================================

def view_all_students():
    """Display all students in the system"""
    print("\n" + "="*50)
    print("List of Students:")
    print("="*50)
    
    for i, name in enumerate(student_names, 1):
        print(f"{i}. {name}")
    
    print("="*50)


def add_new_student():
    """Add a new student to the system"""
    print("\n" + "="*50)
    print("Add New Student")
    print("="*50)
    
    try:
        name = input("Enter name: ")
        matric = input("Enter matric number: ")
        
        age_str = input("Enter age: ")
        age = int(age_str)
        if not (16 <= age <= 40):
            print("✗ Invalid age! Age must be between 16 and 40.")
            return
        
        cgpa_str = input("Enter CGPA: ")
        cgpa = float(cgpa_str)
        if not (0.0 <= cgpa <= 5.0):
            print("✗ Invalid CGPA! CGPA must be between 0.0 and 5.0.")
            return
        
        active_input = input("Is the student active (yes/no): ").lower()
        is_active = active_input in ["yes", "y"]
        
        courses_input = input("Enter courses (comma separated): ")
        courses = [course.strip() for course in courses_input.split(",")]
        
        # Create grades dictionary (simplified - would need actual scores)
        grades = {}
        scores = {}
        for course in courses:
            # For simplicity, assign a default grade based on CGPA
            if cgpa >= 4.5:
                grades[course] = "A"
                scores[course] = 90
            elif cgpa >= 3.5:
                grades[course] = "B"
                scores[course] = 80
            elif cgpa >= 2.5:
                grades[course] = "C"
                scores[course] = 70
            else:
                grades[course] = "D"
                scores[course] = 60
        
        # Add to data structures
        student_names.append(name)
        students_data[name] = {
            "matric": matric,
            "age": age,
            "cgpa": cgpa,
            "is_active": is_active,
            "courses": courses,
            "grades": grades,
            "scores": scores
        }
        
        # Update unique courses set
        unique_courses.update(courses)
        
        print(f"\n✓ Student record added successfully.")
        print(f"  Name: {name}")
        print(f"  Matric: {matric}")
        print(f"  CGPA: {cgpa}")
        
    except ValueError:
        print("✗ Invalid input! Please enter valid numbers for age and CGPA.")
    except Exception as e:
        print(f"✗ Error adding student: {e}")


def check_eligibility_for_graduation():
    """
    Task 4.2: Eligibility Checker
    Uses logical operators (and, or) to determine if a student is eligible for graduation.
    A student is eligible if:
    - CGPA is 2.5 or above
    - There are no outstanding courses (all courses completed)
    - Is_active is True
    """
    print("\n" + "="*50)
    print("Check Eligibility for Graduation")
    print("="*50)
    
    name = input("Enter student name: ")
    
    if name not in students_data:
        print(f"✗ Student '{name}' not found in the system.")
        return
    
    student = students_data[name]
    
    print(f"\nChecking eligibility...")
    print(f"Matric Number: {student['matric']}")
    print(f"CGPA: {student['cgpa']}")
    print(f"Outstanding Courses: 0")  # Simplified - assuming all courses are completed
    print(f"Active Status: {student['is_active']}")
    
    # Eligibility check using logical operators
    cgpa_eligible = student['cgpa'] >= 2.5
    no_outstanding = True  # Simplified - would check actual outstanding courses
    is_active = student['is_active']
    
    eligible = cgpa_eligible and no_outstanding and is_active
    
    print("\n" + "-"*50)
    print("Eligibility Result:")
    print("-"*50)
    
    if eligible:
        print(f"✓ {name} is eligible for graduation.")
    else:
        reasons = []
        if not cgpa_eligible:
            reasons.append("CGPA below 2.5")
        if not no_outstanding:
            reasons.append("has outstanding courses")
        if not is_active:
            reasons.append("student is not active")
        
        print(f"✗ {name} is NOT eligible for graduation.")
        print(f"  Reasons: {', '.join(reasons)}")


def find_top_performer():
    """Find the student with the highest CGPA"""
    print("\n" + "="*50)
    print("Top Performer")
    print("="*50)
    
    if not students_data:
        print("No students in the system.")
        return
    
    top_student = None
    top_cgpa = 0.0
    
    for name, data in students_data.items():
        if data['cgpa'] > top_cgpa:
            top_cgpa = data['cgpa']
            top_student = name
    
    if top_student:
        student = students_data[top_student]
        print(f"\nName: {top_student}")
        print(f"Matric: {student['matric']}")
        print(f"CGPA: {student['cgpa']}")
        print(f"Courses: {student['courses']}")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("Menu Options")
    print("="*50)
    print("1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Exit")
    print("="*50)


def run_menu_system():
    """
    Task 4.1: Build a Console Menu
    Create a menu using MATCH CASE with options
    The menu should repeat until the user selects Exit
    """
    print("\n" + "="*50)
    print("     Student Academic Performance System")
    print("="*50)
    print("Loading student records...")
    print(f"{len(students_data)} student profiles loaded successfully.")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice: ").strip()
            
            match choice:
                case "1":
                    view_all_students()
                case "2":
                    add_new_student()
                case "3":
                    check_eligibility_for_graduation()
                case "4":
                    find_top_performer()
                case "5":
                    print("\nExiting the system...")
                    print("Goodbye!")
                    break
                case _:
                    print("\n✗ Invalid choice! Please enter a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\n\nExiting the system...")
            print("Goodbye!")
            break
        except Exception as e:
            print(f"\n✗ An error occurred: {e}")


# ============================================================================
# PART 5: ADVANCED CHALLENGES (Optional)
# ============================================================================

def calculate_average_scores():
    """
    Task 5.1: Nested Data Processing
    Given a nested dictionary of students and their scores:
    - Calculate the average score for each student
    - Identify students who scored above 70 in all registered courses
    """
    print("\n" + "="*50)
    print("Average Scores Analysis")
    print("="*50)
    
    student_averages = {}
    students_above_70 = []
    
    for name, data in students_data.items():
        scores = data.get("scores", {})
        
        if scores:
            # Calculate average score
            total = sum(scores.values())
            average = total / len(scores)
            student_averages[name] = average
            
            # Check if all scores are above 70
            all_above_70 = all(score > 70 for score in scores.values())
            if all_above_70:
                students_above_70.append(name)
    
    print("\nAverage Scores per Student:")
    for name, avg in sorted(student_averages.items(), key=lambda x: x[1], reverse=True):
        print(f"  {name}: {avg:.2f}")
    
    print("\nStudents who scored above 70 in all courses:")
    if students_above_70:
        for name in students_above_70:
            print(f"  ✓ {name}")
    else:
        print("  None")
    
    return student_averages, students_above_70


def identify_data_type(data):
    """
    Task 5.2: Pattern Matching with MATCH CASE
    Write a function that uses MATCH CASE to identify the type of a given input.
    The function should detect: int, float, list, dict, str
    """
    match type(data).__name__:
        case "int":
            return {
                "type": "Integer",
                "description": f"Whole number: {data}",
                "example_use": "Used for counting, indexing, and age values"
            }
        case "float":
            return {
                "type": "Float",
                "description": f"Decimal number: {data}",
                "example_use": "Used for CGPA, percentages, and precise measurements"
            }
        case "list":
            return {
                "type": "List",
                "description": f"Ordered collection with {len(data)} items",
                "example_use": "Used for storing multiple courses or scores"
            }
        case "dict":
            return {
                "type": "Dictionary",
                "description": f"Key-value pairs with {len(data)} entries",
                "example_use": "Used for storing student profiles and grades"
            }
        case "str":
            return {
                "type": "String",
                "description": f"Text data: '{data}'",
                "example_use": "Used for names, matric numbers, and descriptions"
            }
        case _:
            return {
                "type": "Unknown",
                "description": f"Type: {type(data).__name__}",
                "example_use": "Unsupported data type"
            }


def demonstrate_pattern_matching():
    """Demonstrate the pattern matching function"""
    print("\n" + "="*50)
    print("Pattern Matching Demonstration")
    print("="*50)
    
    test_data = [
        25,  # int
        3.75,  # float
        ["Python", "Statistics"],  # list
        {"name": "John", "age": 20},  # dict
        "Hello World"  # str
    ]
    
    for data in test_data:
        result = identify_data_type(data)
        print(f"\nInput: {data}")
        print(f"  Type: {result['type']}")
        print(f"  Description: {result['description']}")
        print(f"  Example Use: {result['example_use']}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run the program"""
    # Display department information
    dept_name, faculty, year = department_info
    print(f"\nDepartment: {dept_name}")
    print(f"Faculty: {faculty}")
    print(f"Year: {year}")
    
    # Demonstrate some features before menu
    print("\n" + "="*50)
    print("Demonstrating Key Features")
    print("="*50)
    
    # Demonstrate grading function
    print("\n--- Grading Function Example ---")
    test_score = 85
    grade = get_grade(test_score)
    feedback = get_grade_feedback(grade)
    print(f"Score: {test_score} → Grade: {grade}")
    print(f"Feedback: {feedback}")
    
    # Demonstrate list operations
    demonstrate_list_operations()
    
    # Demonstrate set operations
    demonstrate_set_operations()
    
    # Demonstrate pattern matching
    demonstrate_pattern_matching()
    
    # Run the main menu system
    run_menu_system()


if __name__ == "__main__":
    main()

