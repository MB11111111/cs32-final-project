import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# Load and clean data
def load_data(filename):
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        print("Error: File not found.")
        exit()

    # Check required columns
    required_cols = ["Exercise_hours_per_week", "BMI", "Sleep_hours_per_night"]
    for col in required_cols:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Handle missing data
    data["Exercise_hours_per_week"] = data["Exercise_hours_per_week"].fillna(0)
    data["BMI"] = data["BMI"].fillna(data["BMI"].mean())
    data["Sleep_hours_per_night"] = data["Sleep_hours_per_night"].fillna(data["Sleep_hours_per_night"].mean())

    return data


# Add user input (NEW FEATURE)
def add_user_entry(data):
    print("\n--- Add New Entry ---")

    name = input("Enter name: ")

    # Input validation
    while True:
        try:
            exercise = float(input("Enter exercise hours per week: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            bmi = float(input("Enter BMI: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            sleep = float(input("Enter sleep hours per night: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Add timestamp
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_row = pd.DataFrame({
        "Name": [name],
        "Exercise_hours_per_week": [exercise],
        "BMI": [bmi],
        "Sleep_hours_per_night": [sleep],
        "Date": [date]
    })

    data = pd.concat([data, new_row], ignore_index=True)

    # Save updated dataset
    data.to_csv("sample_lifestyle.csv", index=False)

    print("Entry added successfully!")

    return data


# Interpret correlation
def interpret_correlation(corr, label):
    if corr > 0.5:
        print(f"There is a strong positive relationship between {label}.")
    elif corr < -0.5:
        print(f"There is a strong negative relationship between {label}.")
    else:
        print(f"There is a weak or no clear relationship between {label}.")


# Analyze data
def analyze_data(data):
    print("\nHere is the dataset:")
    print(data)

    exercise = data["Exercise_hours_per_week"]
    bmi = data["BMI"]
    sleep = data["Sleep_hours_per_night"]

    # Stats
    print("\nExercise stats:")
    print(exercise.describe())

    print("\nBMI stats:")
    print(bmi.describe())

    print("\nSleep stats:")
    print(sleep.describe())

    # Correlations
    exercise_corr = exercise.corr(bmi)
    sleep_corr = sleep.corr(bmi)

    print("\nCorrelation between exercise and BMI:", exercise_corr)
    print("Correlation between sleep and BMI:", sleep_corr)

    # Interpret results
    print("\nInterpretation:")
    interpret_correlation(exercise_corr, "exercise and BMI")
    interpret_correlation(sleep_corr, "sleep and BMI")

    # BMI category
    avg_bmi = bmi.mean()
    print(f"\nAverage BMI: {avg_bmi:.2f}")

    if avg_bmi < 18.5:
        print("Average BMI is underweight.")
    elif avg_bmi < 25:
        print("Average BMI is in the healthy range.")
    elif avg_bmi < 30:
        print("Average BMI is overweight.")
    else:
        print("Average BMI is in the obese range.")

    return exercise, sleep, bmi


# Plot data
def plot_data(exercise, sleep, bmi):
    # Exercise vs BMI
    plt.figure()
    plt.scatter(exercise, bmi)
    plt.xlabel("Exercise Hours per Week")
    plt.ylabel("BMI")
    plt.title("Exercise vs BMI")
    plt.savefig("exercise_vs_bmi.png")

    # Sleep vs BMI
    plt.figure()
    plt.scatter(sleep, bmi)
    plt.xlabel("Sleep Hours per Night")
    plt.ylabel("BMI")
    plt.title("Sleep vs BMI")
    plt.savefig("sleep_vs_bmi.png")

    print("\nPlots saved as:")
    print("exercise_vs_bmi.png")
    print("sleep_vs_bmi.png")


# ---------------------------
# Main program
# ---------------------------
def main():
    data = load_data("sample_lifestyle.csv")

    choice = input("Do you want to add a new entry? (yes/no): ")

    if choice.lower() == "yes":
        data = add_user_entry(data)

    exercise, sleep, bmi = analyze_data(data)
    plot_data(exercise, sleep, bmi)


# Run program
if __name__ == "__main__":
    main()
