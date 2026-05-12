# Git Tutorials

This is a simple Python project created to practice Git and GitHub.

The project loads a small student grades dataset and computes basic statistics such as:

- Average grade per student
- Best student
- Class average
- Subject averages

## Project Structure

Git-Tutorials/
│
├── data/
│   └── students.csv
│
├── src/
│   ├── load_data.py
│   └── analyze_data.py
│
└── README.md

## Dataset

The dataset is located in:

data/students.csv

It contains student grades in three subjects:

- Math
- English
- Programming

Example:

name,math,english,programming
Ralph,85,78,92
Maya,90,88,84
Karim,70,75,80

## How to Run the Project

First, open a terminal inside the project folder:

Git-Tutorials/

Run the first script to load and display the dataset:

python src/load_data.py

Run the second script to analyze the dataset:

python src/analyze_data.py

## Expected Output

The analysis script prints:

- The dataset with an average grade for each student
- The best student
- The class average
- The average grade per subject

Example output:

Best student:
Sara with an average of 91.33

Class average:
83.92

Subject averages:
Math: 84.50
English: 82.13
Programming: 84.25

## Purpose of This Project

The goal of this project is to practice a complete Git and GitHub workflow:

- Creating a local project
- Adding files and folders
- Tracking changes with Git
- Writing a README file
- Making commits
- Pushing the project to GitHub