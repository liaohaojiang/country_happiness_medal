import pandas as pd

# Load the cleaned and production CSV file from the provided GitHub URL
csv_url = 'https://raw.githubusercontent.com/dcrefugee/country_happiness_medal/main/2024%20Medal%20and%20WHR%20Master%20Table.csv'

# Read the CSV file
data = pd.read_csv(csv_url)

# Display the first few rows to explore the structure of the data
print(data.head())

# Load the relevant sheet into a DataFrame
df = data

# Display the first few rows of the dataset to understand its structure
df.head()

# Selecting relevant columns for correlation analysis
correlation_data = df[['total_medals', 'Ladder score', 'Explained by: Log GDP per capita', 
                       'Explained by: Social support', 'Explained by: Healthy life expectancy', 
                       'Explained by: Perceptions of corruption']]

# Calculating the correlation matrix
correlation_matrix = correlation_data.corr()

# Display the correlation matrix to analyze relationships
correlation_matrix
