import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
data = pd.read_csv("sample_lifestyle.csv")

# Step 2: Check the data
print("Here is the dataset:")
print(data)

# Step 3: Extract columns
exercise = data["Exercise_hours_per_week"]
bmi = data["BMI"]

# Step 4: Basic statistics
print("\nExercise stats:")
print(exercise.describe())

print("\nBMI stats:")
print(bmi.describe())

# Step 5: Scatterplot
plt.scatter(exercise, bmi)
plt.xlabel("Exercise Hours per Week")
plt.ylabel("BMI")
plt.title("Exercise vs BMI")
plt.show()

# Step 6: Correlation
correlation = exercise.corr(bmi)
print("\nCorrelation between exercise and BMI:", correlation)
