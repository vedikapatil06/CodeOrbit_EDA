# Exploratory Data Analysis (EDA)

## 1. Introduction

This project was completed as part of the CodeOrbit Tech Data Science Internship. The objective was to perform Exploratory Data Analysis on a student performance dataset using Python, Pandas, Matplotlib, and Seaborn.

EDA was performed to understand the distribution of student marks, attendance, and age and to identify relationships between the variables.

## 2. Dataset

The dataset contains the following columns:

* Student_ID
* Name
* Age
* Marks
* Attendance

After removing the duplicate record and handling missing/incorrect values, the dataset contained 10 unique student records.

## 3. Data Preparation

Before performing EDA:

* The Age column was converted to numeric format.
* The invalid Age value was handled as a missing value.
* Missing Age and Marks values were replaced using their median values.
* The duplicate record was removed.

## 4. Visualizations

The following visualizations were created:

### Marks Distribution Histogram

The histogram shows the distribution of student marks. Marks range from 68 to 95, with an average of 81.6.

### Marks by Student Bar Chart

The bar chart compares the marks obtained by individual students and makes it easy to identify students with relatively high and low marks.

### Marks vs Attendance Scatter Plot

The scatter plot shows the relationship between attendance and marks. The points indicate a strong positive relationship between the two variables.

### Age Distribution

The age distribution shows that most students are 21 years old.

## 5. Summary Statistics

| Statistic |  Age | Marks | Attendance |
| --------- | ---: | ----: | ---------: |
| Mean      | 20.9 |  81.6 |       88.0 |
| Minimum   |   20 |    68 |         75 |
| Maximum   |   22 |    95 |         96 |

## 6. Correlation Analysis

The correlation between Marks and Attendance was **0.946**, indicating a strong positive relationship in this dataset.

The correlation between Age and Marks was **-0.658**, while the correlation between Age and Attendance was **-0.562**.

These correlations describe relationships in this dataset and should not be interpreted as proof of causation.

## 7. Key Findings

1. The average student mark is 81.6.
2. Student marks range from 68 to 95.
3. The average attendance is 88%.
4. Most students in the dataset are 21 years old.
5. Marks and attendance have a strong positive correlation of 0.946.
6. No major extreme outlier was identified from the basic statistical summary.
7. The dataset is small, so the findings should not be generalized to a larger student population.

## 8. Conclusion

The EDA helped identify distributions, relationships, and patterns within the student performance dataset. The strongest observed relationship was between attendance and marks. The visualizations and statistical analysis provide a simple understanding of student performance and demonstrate the use of Pandas, Matplotlib, and Seaborn for exploratory data analysis.
