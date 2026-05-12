import pandas as pd


def load_students_data(filepath):
    """
    Load the students dataset from a CSV file.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded dataset.
    """
    data = pd.read_csv(filepath)
    return data


if __name__ == "__main__":
    df = load_students_data("data/students.csv")
    print("Students dataset:")
    print(df)