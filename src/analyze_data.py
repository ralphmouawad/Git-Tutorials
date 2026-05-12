from load_data import load_students_data


def compute_average_grade(row):
    """
    Compute the average grade for one student.
    """
    return (row["math"] + row["english"] + row["programming"]) / 3


def analyze_students(filepath):
    """
    Load the students dataset and print useful summary results.
    """
    df = load_students_data(filepath)

    # Add an average column for each student
    df["average"] = df.apply(compute_average_grade, axis=1)

    # Find the best student
    best_student = df.loc[df["average"].idxmax()]

    # Compute class average
    class_average = df["average"].mean()

    # Compute subject averages
    math_average = df["math"].mean()
    english_average = df["english"].mean()
    programming_average = df["programming"].mean()

    print("Students dataset with average grade:")
    print(df)

    print("\nBest student:")
    print(f"{best_student['name']} with an average of {best_student['average']:.2f}")

    print("\nClass average:")
    print(f"{class_average:.2f}")

    print("\nSubject averages:")
    print(f"Math: {math_average:.2f}")
    print(f"English: {english_average:.2f}")
    print(f"Programming: {programming_average:.2f}")


if __name__ == "__main__":
    analyze_students("data/students.csv")