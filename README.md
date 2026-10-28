# CodeOrbit Tech - Exploratory Data Analysis

## About the Project

This project was completed as part of the **CodeOrbit Tech Data Science Internship**.

The objective is to perform Exploratory Data Analysis (EDA) on a student performance dataset using Python, Pandas, Matplotlib, and Seaborn.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Dataset

The dataset contains:

* `Student_ID`
* `Name`
* `Age`
* `Marks`
* `Attendance`

After data preparation, the dataset contains 10 unique student records.

## EDA Performed

The project includes:

1. Dataset inspection and summary statistics
2. Marks distribution histogram
3. Marks by student bar chart
4. Marks vs Attendance scatter plot
5. Age distribution chart
6. Correlation analysis

## Key Findings

* Average marks: **81.6**
* Average attendance: **88%**
* Highest marks: **95**
* Lowest marks: **68**
* Marks and attendance show a strong positive correlation of **0.946**.
* Most students are 21 years old.

The correlation indicates a relationship within this dataset and does not establish causation.

## Project Structure

```text
CodeOrbit_EDA/
│
├── data/
│   └── student_performance.csv
│
├── output/
│   ├── marks_distribution.png
│   ├── marks_by_student.png
│   ├── marks_vs_attendance.png
│   └── age_distribution.png
│
├── eda_analysis.py
├── Task2_Report.md
├── README.md
└── requirements.txt
```

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python eda_analysis.py
```

The generated visualizations are saved in the `output` folder.

## Conclusion

The project demonstrates how Exploratory Data Analysis can be used to understand data distributions, identify patterns, and examine relationships between variables using Pandas, Matplotlib, and Seaborn.
