import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/student_performance.csv")

# Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Fill missing values for analysis
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Remove duplicate records
df = df.drop_duplicates()

print("========== DATASET ==========")
print(df)

print("\n========== BASIC INFORMATION ==========")
print(df.info())

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe())

# --------------------------------------------------
# 1. Histogram - Marks Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.savefig("output/marks_distribution.png")
plt.show()

# --------------------------------------------------
# 2. Bar Chart - Student Marks
# --------------------------------------------------

plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Marks by Student")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/marks_by_student.png")
plt.show()

# --------------------------------------------------
# 3. Scatter Plot - Marks vs Attendance
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Marks vs Attendance")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.tight_layout()

plt.savefig("output/marks_vs_attendance.png")
plt.show()

# --------------------------------------------------
# 4. Age Distribution
# --------------------------------------------------

plt.figure(figsize=(7, 5))
sns.countplot(x="Age", data=df)
plt.title("Age Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.savefig("output/age_distribution.png")
plt.show()

# --------------------------------------------------
# 5. Correlation
# --------------------------------------------------

print("\n========== CORRELATION ==========")
print(df[["Age", "Marks", "Attendance"]].corr())

print("\nEDA completed successfully!")