# Lifestyle Tracker Project

## Description

This project is a lifestyle tracker that analyzes relationships between exercise, sleep, and BMI. It is designed to not only compute statistics, but also interpret results so that users without a statistics background can understand the data.

The program:

* Loads a dataset from a CSV file
* Cleans missing or incomplete data
* Computes summary statistics
* Calculates correlations between lifestyle variables and BMI
* Generates visualizations (scatterplots)
* Provides plain-language interpretations of results

## Features

* Handles missing data using safe defaults
* Analyzes:

  * Exercise vs BMI
  * Sleep vs BMI
* Generates scatterplots saved as image files
* Interprets correlations (strong/weak, positive/negative)
* Classifies average BMI into health categories


## How to Run

### 1. Install Dependencies

Make sure you have Python installed, then run:

```
pip install pandas matplotlib
```

### 2. Required Files

Ensure the following files are in the same folder:

* `tracker.py` (main program)
* `sample_lifestyle.csv` (dataset)

### 3. Run the Program

In your terminal, navigate to the project folder and run:

```
python3 tracker.py
```


## Dataset Format

The CSV file must include the following columns:

```
Name,Exercise_hours_per_week,BMI,Sleep_hours_per_night
```

### Example:

```
Alice,3,22.5,7
Bob,1,27.3,5
Charlie,5,24.0,6
Dana,0,30.1,4
Eli,4,23.5,8
```

## Output

The program generates:

* `exercise_vs_bmi.png`
* `sleep_vs_bmi.png`

And prints:

* Summary statistics
* Correlation values
* Plain-language interpretations


## Project Structure

* `tracker.py` → main script containing data loading, analysis, and visualization
* `sample_lifestyle.csv` → input dataset
* `.png files` → generated plots


## Acknowledgments

* Libraries used:

  * pandas
  * matplotlib


## Future Improvements

* Allow users to input their own data
* Track changes over time instead of static analysis
* Add more advanced statistical analysis or visualizations
