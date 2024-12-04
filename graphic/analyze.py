import pandas as pd

# Specify the paths to your CSV files
usage_csv_file_path = '/Users/vagouz/Downloads/usage.csv'
error_csv_file_path = '/Users/vagouz/Downloads/error.csv'

# Read the CSV files into DataFrames
df_usage = pd.read_csv(usage_csv_file_path)
df_error = pd.read_csv(error_csv_file_path)

# Merge the DataFrames on 'type'
merged_df = pd.merge(df_usage, df_error, on='type', how='left')

# Calculate the error ratio
merged_df['error-ratio'] = merged_df['error-count'] / merged_df['usage-count']

# Fill NaN values with 0 for devices with no errors reported
merged_df['error-count'] = merged_df['error-count'].fillna(0)
merged_df['error-ratio'] = merged_df['error-ratio'].fillna(0)

# Print the merged DataFrame with error ratio
print("Merged DataFrame with Error Ratio:")
print(merged_df)

# Sort the DataFrame by 'error-ratio' in descending order
sorted_df = merged_df.sort_values(by='error-ratio', ascending=False)

# Print the sorted DataFrame
print("\nSorted DataFrame by Error Ratio (descending):")
print(sorted_df)

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv('/Users/vagouz/Downloads/sorted_by_error_ratio.csv', index=False)