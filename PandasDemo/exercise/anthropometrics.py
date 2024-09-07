import pandas as pd

dataFileName = 'sample_data.csv'
anthropometrics = pd.read_csv(dataFileName)
print("Read file", dataFileName, "file.")
print(anthropometrics)

# Display the first 5 rows of the DataFrame.
print("First 5 rows")
print(anthropometrics.head(5))

# Display the column names and data types.
print("Column names and data types")
print(anthropometrics.dtypes)

# Display the summary statistics of the DataFrame.
print("Summary statistic")
print(anthropometrics.describe())

# Find the number of rows and columns in the DataFrame.
rowCount, colCount = anthropometrics.shape
print(f"Dataframe has {rowCount} rows and {colCount} columns.")

# Rename the columns to Height and Weight.
anthropometrics.columns = ['Index','Height', 'Weight']
print("Column names and data types")
print(anthropometrics.dtypes)

# Add a new column Height_in_meters by converting the Height 
# from inches to meters (1 inch = 0.0254 meters).
anthropometrics['Height (meters)'] = anthropometrics['Height'] * 0.0254
print(anthropometrics)

# Filter and display the rows where the Weight is greater than 150 pounds.
filtered_anthropometrics = anthropometrics[anthropometrics['Weight'] > 150]
print("Filtered anthropometrics")
print(filtered_anthropometrics)