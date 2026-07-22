"""
=============================================================
        STUDENT REPORT CARD GENERATOR
=============================================================

This program generates a comprehensive student report card.
It collects student information, subject scores, calculates
grades, determines class position, and displays a formatted
report card.

Concepts Used:
    - Variables and Data Types
    - Input and Output
    - Lists and the in keyword
    - For loops and While loops
    - Conditional Statements (if, elif, else)
    - Functions
    - String Formatting

Author: Python Beginners Class
=============================================================
"""


# ============================================================
# SECTION 1: GRADING SYSTEM DEFINITION
# ============================================================
# We define the grade boundaries using lists.
# Each grade has a minimum score, maximum score, and letter grade.
# The 'in' keyword will be used later to check score ranges.
# ============================================================

grade_letters = ["A", "B", "C", "D", "F"]
grade_ranges = [(80, 100), (60, 79), (40, 59), (30, 39), (0, 29)]
grade_descriptions = ["Excellent", "Very Good", "Good", "Fair", "Fail"]


def get_grade(score):
    """
    This function takes a score and returns the grade letter.
    It uses the in keyword and zip to match scores to grades.
    """
    for i in range(len(grade_letters)):
        min_score, max_score = grade_ranges[i]
        if min_score <= score <= max_score:
            return grade_letters[i]
    return "F"


def get_remark(grade):
    """
    This function takes a grade letter and returns a remark.
    It uses the in keyword to check if grade is in our list.
    """
    remarks = {
        "A": "Excellent work! Keep it up!",
        "B": "Very good performance. Well done!",
        "C": "Good effort. There is room for improvement.",
        "D": "Fair performance. More effort is needed.",
        "F": "Poor performance. Serious improvement needed."
    }
    return remarks.get(grade, "No remark available")


def get_teacher_comment(score):
    """
    This function generates a teacher comment based on score.
    It demonstrates the use of if, elif, and else statements.
    """
    if score >= 80:
        return "Outstanding performance in this subject."
    elif score >= 60:
        return "Good performance. Keep working hard."
    elif score >= 40:
        return "Average performance. Needs more practice."
    elif score >= 30:
        return "Below average. Must put in more effort."
    else:
        return "Needs significant improvement. See the teacher."


# ============================================================
# SECTION 2: STUDENT INFORMATION COLLECTION
# ============================================================
# We collect basic student details using the input() function.
# Variables store the student's name, class, and term.
# These are stored as strings since they are text data.
# ============================================================

print("\n" + "=" * 50)
print("   STUDENT REPORT CARD SYSTEM")
print("=" * 50)

student_name = input("\nEnter student name: ").strip()
student_class = input("Enter class (e.g., JSS1A): ").strip()
student_term = input("Enter term (e.g., First Term): ").strip()
student_year = input("Enter academic year (e.g., 2024/2025): ").strip()

# ============================================================
# SECTION 3: NUMBER OF STUDENTS IN CLASS
# ============================================================
# We need to know the total number of students in the class
# so we can calculate the student's position later.
# The position is determined by comparing scores with others.
# ============================================================

total_students = int(input("Enter total number of students in class: "))

# ============================================================
# SECTION 4: SUBJECTS AND SCORES INPUT
# ============================================================
# We use a list to store all subjects and their scores.
# A for loop is used to collect data for each subject.
# Each subject's data is stored as a dictionary inside a list.
# The 'in' keyword checks if a subject already exists.
# ============================================================

num_subjects = int(input("\nEnter number of subjects: "))

# Empty list to store all subject data
subjects_data = []

print("\n--- Enter Scores for Each Subject ---")

for i in range(num_subjects):
    print(f"\nSubject {i + 1} of {num_subjects}")

    subject_name = input("  Enter subject name: ").strip()

    # Check if subject already exists using the in keyword
    # This prevents duplicate subjects from being added
    existing_subjects = []
    for item in subjects_data:
        existing_subjects.append(item["name"])

    if subject_name in existing_subjects:
        print(f"  Warning: '{subject_name}' already exists. Skipping.")
        continue

    # Collect test and exam scores
    # We use float() to allow decimal scores like 45.5
    test_score = float(input(f"  Enter test score for {subject_name} (out of 30): "))
    exam_score = float(input(f"  Enter exam score for {subject_name} (out of 70): "))

    # Validate that scores are within acceptable ranges
    if test_score < 0 or test_score > 30:
        print("  Error: Test score must be between 0 and 30.")
        print("  Setting test score to 0.")
        test_score = 0

    if exam_score < 0 or exam_score > 70:
        print("  Error: Exam score must be between 0 and 70.")
        print("  Setting exam score to 0.")
        exam_score = 0

    # Calculate total score and grade
    total_score = test_score + exam_score
    grade = get_grade(total_score)
    remark = get_remark(grade)
    teacher_comment = get_teacher_comment(total_score)

    # Store subject data as a dictionary in the subjects_data list
    subject_record = {
        "name": subject_name,
        "test_score": test_score,
        "exam_score": exam_score,
        "total_score": total_score,
        "grade": grade,
        "remark": remark,
        "teacher_comment": teacher_comment
    }

    subjects_data.append(subject_record)

    print(f"  -> {subject_name}: Total = {total_score}, Grade = {grade}")


# ============================================================
# SECTION 5: CALCULATE STUDENT AVERAGE
# ============================================================
# We calculate the student's overall average score.
# A while loop sums all total scores from each subject.
# The average helps determine the student's general performance.
# ============================================================

total_all_scores = 0
subject_index = 0

while subject_index < len(subjects_data):
    total_all_scores += subjects_data[subject_index]["total_score"]
    subject_index += 1

# Calculate average using the total score and number of subjects
average_score = total_all_scores / len(subjects_data) if len(subjects_data) > 0 else 0
overall_grade = get_grade(average_score)


# ============================================================
# SECTION 6: DETERMINE CLASS POSITION
# ============================================================
# The student's position is simulated based on their average.
# We use the total_students input to determine a position.
# A higher average score means a better (lower number) position.
# The 'in' keyword checks if the grade is in our grade list.
# ============================================================

# Simulate position based on average score
# In a real system, this would compare with other students
if overall_grade in grade_letters:
    grade_index = grade_letters.index(overall_grade)
    # Calculate approximate position using grade index and average
    position_out_of = total_students
    if grade_index == 0:
        # Grade A - top positions (1st to 15% of class)
        max_position = max(1, int(total_students * 0.15))
        position = 1
    elif grade_index == 1:
        # Grade B - upper positions (15% to 40% of class)
        min_pos = int(total_students * 0.15) + 1
        max_pos = int(total_students * 0.40)
        position = min_pos
    elif grade_index == 2:
        # Grade C - middle positions (40% to 65% of class)
        min_pos = int(total_students * 0.40) + 1
        max_pos = int(total_students * 0.65)
        position = min_pos
    elif grade_index == 3:
        # Grade D - lower positions (65% to 85% of class)
        min_pos = int(total_students * 0.65) + 1
        max_pos = int(total_students * 0.85)
        position = min_pos
    else:
        # Grade F - bottom positions (85% to 100% of class)
        min_pos = int(total_students * 0.85) + 1
        position = min_pos
else:
    position = total_students

# Add ordinal suffix to position number (1st, 2nd, 3rd, 4th, etc.)
def get_ordinal_suffix(number):
    """
    This function returns the ordinal suffix for a number.
    For example: 1 -> 'st', 2 -> 'nd', 3 -> 'rd', 4 -> 'th'
    """
    if 11 <= (number % 100) <= 13:
        return "th"
    else:
        last_digit = number % 10
        if last_digit == 1:
            return "st"
        elif last_digit == 2:
            return "nd"
        elif last_digit == 3:
            return "rd"
        else:
            return "th"


position_suffix = get_ordinal_suffix(position)
position_str = f"{position}{position_suffix}"


# ============================================================
# SECTION 7: DISPLAY THE REPORT CARD
# ============================================================
# We display the formatted report card using print statements.
# String formatting with f-strings makes the output readable.
# A for loop iterates through all subjects to display scores.
# The 'in' keyword checks grade validity before display.
# ============================================================

print("\n")
print("=" * 60)
print(" " * 15 + "STUDENT REPORT CARD")
print("=" * 60)

# Student Information Section
print(f"\n  Student Name    : {student_name}")
print(f"  Class           : {student_class}")
print(f"  Term            : {student_term}")
print(f"  Academic Year   : {student_year}")
print(f"  Position        : {position_str} out of {total_students} students")

print("\n" + "-" * 60)
print(" " * 15 + "SUBJECT PERFORMANCE")
print("-" * 60)

# Table Header
print(f"\n  {'Subject':<15} {'Test(30)':<10} {'Exam(70)':<10} {'Total':<8} {'Grade':<7} {'Remark'}")
print("  " + "-" * 55)

# Display each subject's performance using a for loop
for subject in subjects_data:
    # The 'in' keyword checks if grade is valid
    if subject["grade"] in grade_letters:
        print(f"  {subject['name']:<15} {subject['test_score']:<10.1f} "
              f"{subject['exam_score']:<10.1f} {subject['total_score']:<8.1f} "
              f"{subject['grade']:<7} {subject['remark']}")

print("  " + "-" * 55)

# Overall Performance Section
print(f"\n  Overall Average : {average_score:.1f}")
print(f"  Overall Grade   : {overall_grade}")
print(f"  Overall Remark  : {get_remark(overall_grade)}")

print("\n" + "-" * 60)
print(" " * 10 + "TEACHER'S REMARKS AND COMMENTS")
print("-" * 60)

# Display teacher comments for each subject
for subject in subjects_data:
    print(f"\n  {subject['name']}:")
    print(f"    Grade: {subject['grade']} | Score: {subject['total_score']:.1f}")
    print(f"    Remark: {subject['remark']}")
    print(f"    Comment: {subject['teacher_comment']}")

print("\n" + "-" * 60)

# Class Teacher's General Comment
print("\n  CLASS TEACHER'S GENERAL COMMENT:")
print("  " + "=" * 50)

# Generate general comment based on overall performance
if overall_grade == "A":
    general_comment = (f"{student_name} has been an outstanding student "
                       f"this {student_term}. Performance is excellent "
                       f"across all subjects. Keep up the great work!")
elif overall_grade == "B":
    general_comment = (f"{student_name} has performed very well this "
                       f"{student_term}. The results show consistency "
                       f"and dedication. Aim for even higher scores.")
elif overall_grade == "C":
    general_comment = (f"{student_name} has shown reasonable performance "
                       f"this {student_term}. There is room for improvement "
                       f"in some subjects. Encourage more studying.")
elif overall_grade == "D":
    general_comment = (f"{student_name}'s performance this {student_term} "
                       f"is below expectations. More effort and dedication "
                       f"is needed. Parents should ensure more supervision.")
else:
    general_comment = (f"{student_name}'s performance this {student_term} "
                       f"is very poor. Urgent improvement is needed. "
                       f"A meeting with parents/guardians is recommended.")

print(f"  {general_comment}")

print("\n" + "=" * 60)
print(" " * 10 + "END OF REPORT CARD")
print("=" * 60)

# ============================================================
# SECTION 8: SUMMARY STATISTICS
# ============================================================
# We display summary statistics about the student's performance.
# This section uses loops and lists to calculate key metrics.
# The 'in' keyword helps count grades and subjects passed.
# ============================================================

print("\n" + "-" * 60)
print(" " * 15 + "PERFORMANCE SUMMARY")
print("-" * 60)

# Count how many subjects the student got each grade
grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for subject in subjects_data:
    if subject["grade"] in grade_count:
        grade_count[subject["grade"]] += 1

# Count subjects passed (grade D and above)
subjects_passed = 0
for subject in subjects_data:
    if subject["grade"] in ["A", "B", "C", "D"]:
        subjects_passed += 1

# Count subjects failed (grade F)
subjects_failed = grade_count["F"]

# Find highest and lowest scores
highest_score = 0
lowest_score = 100
best_subject = ""
worst_subject = ""

for subject in subjects_data:
    if subject["total_score"] > highest_score:
        highest_score = subject["total_score"]
        best_subject = subject["name"]
    if subject["total_score"] < lowest_score:
        lowest_score = subject["total_score"]
        worst_subject = subject["name"]

# Display the summary statistics
print(f"\n  Total Subjects Taken  : {len(subjects_data)}")
print(f"  Subjects Passed       : {subjects_passed}")
print(f"  Subjects Failed       : {subjects_failed}")
print(f"  Highest Score         : {highest_score:.1f} ({best_subject})")
print(f"  Lowest Score          : {lowest_score:.1f} ({worst_subject})")
print(f"  Class Position        : {position_str}")

# Display grade distribution
print(f"\n  Grade Distribution:")
for letter in grade_letters:
    count = grade_count[letter]
    bar = "█" * count  # Visual bar using block characters
    print(f"    Grade {letter}: {count} subject(s) {bar}")

print("\n" + "=" * 60)
print("  Thank you for using the Report Card Generator!")
print("=" * 60 + "\n")

# ============================================================
# END OF PROGRAM
# ============================================================
# This capstone project demonstrates:
#   1. Variables and data types (str, int, float)
#   2. Input/output using input() and print()
#   3. Lists and the in keyword
#   4. For loops and while loops
#   5. Conditional statements (if, elif, else)
#   6. Functions with parameters and return values
#   7. Dictionary data structure
#   8. String formatting with f-strings
#   9. Data validation and error handling
#  10. Program structure and code organization
# ============================================================

