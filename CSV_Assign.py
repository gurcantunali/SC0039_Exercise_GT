#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import sys


# In[2]:


# Check if the user supplied a command-line argument for the input file
if len(sys.argv) != 2:
    print("Usage: python CSV_Assign.py <input_file>")

# Get the input file from the command-line arguments
input_file = sys.argv[1]

# Load the data from the specified file
try:
    counts = pd.read_csv(input_file)
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: File '{input_file}' is empty.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)


# In[3]:


# Open and read the file, displaying the first few rows
with open(input_file, mode='r') as f:
    for i, line in enumerate(f):
        if i < 10:  # Display first 10 rows
            print(line.strip())


# In[4]:


def calculate_segment_length(input_file: str, output_file: str):
    # Open the input CSV file and create the output CSV file
    with open(input_file, mode='r', newline='') as csv_in, open(output_file, mode='w', newline='') as csv_out:
        reader = csv.DictReader(csv_in)
        # Define the fieldnames for the output file including the new seq_length column
        fieldnames = reader.fieldnames + ['seq_length']
        writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
        
        # Write the header row to the output file
        writer.writeheader()
        
        # Process each row in the input file
        for row in reader:
            # Calculate the segment length
            start = int(row['loc.start'])
            end = int(row['loc.end'])
            seq_length = end - start
            
            # Add the calculated length to the row
            row['seq_length'] = seq_length
            
            # Write the row to the output file
            writer.writerow(row)

# Specify input and output file paths
input_file = 'brca_cnvs_tcga-1-2.csv'   # Use the correct file path if different
output_file = 'brca_cnvs_tcga_with_lengths.csv'

# Run the function
calculate_segment_length(input_file, output_file)

# Confirmation message
print(f"The file '{output_file}' has been created with the new 'seq_length' column.")


# In[5]:


#Display the first few rows of the output file
with open(output_file, mode='r') as f:
    for i, line in enumerate(f):
        if i < 10:  # Display first 10 rows
            print(line.strip())


# In[ ]:




