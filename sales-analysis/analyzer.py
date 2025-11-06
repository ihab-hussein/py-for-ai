import os
import pandas as pd
import json
import openpyxl

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")
    
print( "CURRENT WORKING DIRECTORY:", os.getcwd())


file=open("data/sales.csv","r")
content=file.read()



# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")

print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")


# Open terminal in VS Code (Terminal > New Terminal)
#git config --global user.name "ihab-hussein"
#git config --global user.email "ihab.a.hussein@gmail.com"

# ihab-hussein
## Initialize Git in your project
# git init

# # Add all your files
# git add .

# # Create your first commit
# git commit -m "Initial commit"

# # Rename branch to main
# git branch -M main

# # Connect to GitHub with HTTPS (use YOUR username)
# git remote add origin https://github.com/YOUR-USERNAME/python-for-ai.git

# # Push your code
# git push -u origin main