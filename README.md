# Lifestyle Tracker Project

## Description

This project is a lifestyle tracker that analyzes relationships between exercise, sleep, and BMI. It is designed to not only compute statistics, but also interpret results so that users without a statistics background can understand the data.

The program now supports both **data analysis and user tracking**, allowing individuals to input their own data and monitor lifestyle patterns over time.


## Features

* Loads and analyzes a dataset from a CSV file
* Handles missing or incomplete data safely
* Computes summary statistics for:

  * Exercise
  * Sleep
  * BMI
* Calculates correlations:

  * Exercise vs BMI
  * Sleep vs BMI
* Generates scatterplot visualizations
* Provides plain-language interpretations of results
* Allows users to input their own data
* Tracks entries over time using timestamps
* Saves updated data back to the dataset



## How to Run

### 1. Install Dependencies

Make sure Python is installed, then run:

```bash
pip install pandas matplotlib
```



### 2. Required Files

Ensure the following files are in the same folder:

* `tracker.py` (main program)
* `sample_lifestyle.csv` (dataset)



### 3. Run the Program

In your terminal, navigate to the project folder and run:

```bash
python3 tracker.py
```



## Dataset Format

The CSV file must include the following columns:

```
Name,Exercise_hours_per_week,BMI,Sleep_hours_per_night,Date
```

### Example:

```
Alice,3,22.5,7,2026-04-01 10:00:00
Bob,1,27.3,5,2026-04-02 11:30:00
Charlie,5,24.0,6,2026-04-03 09:15:00
Dana,0,30.1,4,2026-04-04 08:45:00
Eli,4,23.5,8,2026-04-05 12:00:00
```



## Output

The program generates:

* `exercise_vs_bmi.png`
* `sleep_vs_bmi.png`

It also prints:

* Summary statistics
* Correlation values
* Plain-language interpretations



## Project Structure

* `tracker.py` → main script (data loading, cleaning, analysis, visualization, and user input)
* `sample_lifestyle.csv` → dataset (updated with user entries over time)
* `.png files` → generated plots



## Key Design Decisions

* Added interpretation of statistical results to improve usability
* Implemented data cleaning to handle missing values
* Designed user input system with error handling to prevent crashes
* Introduced timestamp tracking to support longitudinal data collection



## Acknowledgments
* I used AI to correct my code for adding timestamp tracking using 'satetime' and reviewed and tested it myself so that I understood it.

* Libraries used:
  * pandas
  * matplotlib



## Future Improvements

* Develop a graphical user interface for easier interaction
* Track trends over time using the Date variable
* Add more advanced statistical analysis or predictive features
