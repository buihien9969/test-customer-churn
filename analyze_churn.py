import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Import necessary libraries for data analysis
# pandas: For data manipulation and analysis
# numpy: For numerical operations
# matplotlib and seaborn: For data visualization
# scipy.stats: For statistical tests and calculations

# Load the training and testing datasets from CSV files
# The data is split 80/20 for training and testing
df_train = pd.read_csv('Copy of churn-bigml-80.csv')
df_test = pd.read_csv('Copy of churn-bigml-20.csv')

# Combine both datasets for comprehensive analysis
# axis=0 means we're stacking the dataframes vertically (row-wise)
df = pd.concat([df_train, df_test], axis=0)

# Check unique values in the Churn column to understand its format
# This helps confirm the data type and possible values
print("Unique values in the Churn column:")
print(df['Churn'].unique())

# Convert the Churn column from boolean to numeric (0/1)
# This makes it easier to perform calculations and analysis
df['Churn'] = df['Churn'].map({False: 0, True: 1})

# Display basic information about the dataset
# This provides an overview of the data size and structure
print("Basic information about the dataset:")
print(f"Number of samples: {df.shape[0]}")  # Number of rows (samples)
print(f"Number of features: {df.shape[1]}")  # Number of columns (features)
print("\nColumns in the dataset:")  # List all column names
print(df.columns.tolist())

# Check for missing values in the dataset
# Missing values can affect analysis and need to be handled
print("\nChecking for null values:")
print(df.isnull().sum())  # Count null values in each column

# Generate descriptive statistics for the dataset
# This provides statistical measures like mean, std, min, max for each numeric column
print("\nDescriptive statistics:")
print(df.describe())

# Analyze churn distribution
# Calculate counts and percentages of churned vs non-churned customers
churn_count = df['Churn'].value_counts()  # Count of each churn value (0 or 1)
churn_percentage = df['Churn'].value_counts(normalize=True) * 100  # Convert to percentages
print("\nChurn distribution:")
print(f"Non-churned (0): {churn_count[0]} ({churn_percentage[0]:.2f}%)")  # Non-churned customers
print(f"Churned (1): {churn_count[1]} ({churn_percentage[1]:.2f}%)")  # Churned customers

# Analyze characteristics of each customer group
# Generate descriptive statistics for non-churned customers
print("\nCharacteristics of non-churned customers (Churn = 0):")
print(df[df['Churn'] == 0].describe())

# Generate descriptive statistics for churned customers
print("\nCharacteristics of churned customers (Churn = 1):")
print(df[df['Churn'] == 1].describe())

# Compare features between churned and non-churned groups
# This helps identify which factors might influence customer churn
print("\nComparing features between the two groups:")
# Get all numerical columns except the Churn column
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numerical_cols.remove('Churn')  # Remove the Churn column from the list

# For each numerical feature, compare means between churned and non-churned groups
for col in numerical_cols:
    # Calculate mean values for each group
    mean_non_churn = df[df['Churn'] == 0][col].mean()
    mean_churn = df[df['Churn'] == 1][col].mean()
    # Calculate percentage difference between groups
    diff_percentage = ((mean_churn - mean_non_churn) / mean_non_churn * 100) if mean_non_churn != 0 else 0

    # Perform statistical test to determine if the difference is significant
    # Welch's t-test (equal_var=False) is used to compare means of two independent samples
    t_stat, p_value = stats.ttest_ind(df[df['Churn'] == 0][col], df[df['Churn'] == 1][col], equal_var=False)

    # Print results of the comparison
    print(f"{col}:")
    print(f"  - Mean (Non-churned): {mean_non_churn:.2f}")
    print(f"  - Mean (Churned): {mean_churn:.2f}")
    print(f"  - Difference: {diff_percentage:.2f}%")
    # A p-value < 0.05 indicates statistical significance (95% confidence)
    print(f"  - p-value: {p_value:.4f} {'(Statistically significant)' if p_value < 0.05 else '(Not statistically significant)'}")

# Analyze categorical variables
# These are non-numeric features that need different analysis methods
categorical_cols = ['State', 'International plan', 'Voice mail plan']
print("\nAnalyzing categorical variables:")

# For each categorical feature, analyze churn rates by category
for col in categorical_cols:
    print(f"\n{col}:")
    # Calculate churn rate for each category value
    churn_by_category = df.groupby(col)['Churn'].mean() * 100  # Mean of Churn (0/1) gives proportion of churned customers
    count_by_category = df.groupby(col).size()  # Count customers in each category

    # Print churn rate for each category
    for category, churn_rate in churn_by_category.items():
        count = count_by_category[category]
        print(f"  - {category}: {count} customers, churn rate {churn_rate:.2f}%")

# Correlation analysis
# Measure how strongly each feature correlates with churn
print("\nCorrelation analysis with Churn:")
# Calculate correlation coefficients between each feature and Churn
correlations = df[numerical_cols + ['Churn']].corr()['Churn'].sort_values(ascending=False)
print(correlations)  # Higher absolute values indicate stronger relationships

# Save analysis results to a text file
# This creates a report that can be shared or referenced later
with open('churn_analysis_results.txt', 'w') as f:
    f.write("CUSTOMER CHURN ANALYSIS RESULTS\n\n")

    # Write overview section
    f.write("1. DATASET OVERVIEW\n")
    f.write(f"Number of samples: {df.shape[0]}\n")
    f.write(f"Number of features: {df.shape[1]}\n")
    f.write(f"Churn rate: {churn_percentage[1]:.2f}%\n\n")

    # Sections for detailed analysis
    # These sections would be filled with specific insights from the analysis
    f.write("2. CHARACTERISTICS OF CHURNED CUSTOMERS\n")
    # List notable characteristics of churned customers

    f.write("3. CHARACTERISTICS OF NON-CHURNED CUSTOMERS\n")
    # List notable characteristics of non-churned customers

    f.write("4. COMPARISON BETWEEN GROUPS\n")
    # List important differences between the two groups

# Confirm that the analysis results have been saved
print("\nAnalysis results saved to 'churn_analysis_results.txt'")
