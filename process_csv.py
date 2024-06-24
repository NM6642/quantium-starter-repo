import pandas as pd
import os

# Directory containing the CSV files
data_dir = r'C:\Users\LENOVO\Desktop\SE project'

# List of CSV files
csv_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# Initialize an empty list to hold DataFrames
dfs = []

# Process each CSV file
for file in csv_files:
    # Load the data into a DataFrame
    df = pd.read_csv(os.path.join(data_dir, file))
    
    # Filter for "pink morsel" product
    df = df[df['product'] == 'pink morsel']
    
    # Remove the dollar sign from the price and convert to float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Calculate sales
    df['sales'] = df['quantity'] * df['price']
    
    # Select relevant columns
    df = df[['sales', 'date', 'region']]
    
    # Append the DataFrame to the list
    dfs.append(df)

# Combine all DataFrames
combined_df = pd.concat(dfs)

# Save the combined DataFrame to a new CSV file
output_file = os.path.join(data_dir, 'formatted_sales_data.csv')
combined_df.to_csv(output_file, index=False)

print(f"Formatted data saved to {output_file}")


