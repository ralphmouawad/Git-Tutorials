from load_data import load_students_data


def compute_average_grade(row):
    """
    Compute the average grade for one student.
    """
    return (row["math"] + row["english"] + row["programming"]) / 3


def assign_status(average, passing_grade=70):
    """
    Assign a pass/fail status based on the student's average grade.
    """
    if average >= passing_grade:
        return "Pass"
    return "Fail"


def analyze_students(filepath):
    """
    Load the students dataset and print useful summary results.
    """
    df = load_students_data(filepath)

    # Add an average column for each student
    df["average"] = df.apply(compute_average_grade, axis=1)

    # Add a status column
    df["status"] = df["average"].apply(assign_status)

    # Find the best student
    best_student = df.loc[df["average"].idxmax()]

    # Compute class statistics
    class_average = df["average"].mean()
    class_median = df["average"].median()

    # Compute subject averages
    math_average = df["math"].mean()
    english_average = df["english"].mean()
    programming_average = df["programming"].mean()

    # Count passing and failing students
    passing_students = (df["status"] == "Pass").sum()
    failing_students = (df["status"] == "Fail").sum()

    print("Students dataset with average grade and status:")
    print(df)

    print("\nBest student:")
    print(f"{best_student['name']} with an average of {best_student['average']:.2f}")

    print("\nClass statistics:")
    print(f"Mean average: {class_average:.2f}")
    print(f"Median average: {class_median:.2f}")

    print("\nSubject averages:")
    print(f"Math: {math_average:.2f}")
    print(f"English: {english_average:.2f}")
    print(f"Programming: {programming_average:.2f}")

    print("\nPass/fail summary:")
    print(f"Passing students: {passing_students}")
    print(f"Failing students: {failing_students}")


if __name__ == "__main__":
    analyze_students("data/students.csv")