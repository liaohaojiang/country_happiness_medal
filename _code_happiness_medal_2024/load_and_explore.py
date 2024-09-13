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

## correlation scatterplots

import matplotlib.pyplot as plt
import seaborn as sns

# Set the general style for the plots
sns.set(style="whitegrid")

# Visualization 1: Total Medals vs Ladder Score
plt.figure(figsize=(8, 6))
sns.regplot(x='Ladder score', y='total_medals', data=correlation_data, scatter_kws={'s':50}, line_kws={"color":"red"})
plt.title('Total Medals vs Ladder Score (Happiness)')
plt.xlabel('Ladder Score (Happiness)')
plt.ylabel('Total Medals')
plt.show()

# Visualization 2: Total Medals vs GDP per Capita
plt.figure(figsize=(8, 6))
sns.regplot(x='Explained by: Log GDP per capita', y='total_medals', data=correlation_data, scatter_kws={'s':50}, line_kws={"color":"red"})
plt.title('Total Medals vs GDP per Capita')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Total Medals')
plt.show()

# Visualization 3: Total Medals vs Social Support
plt.figure(figsize=(8, 6))
sns.regplot(x='Explained by: Social support', y='total_medals', data=correlation_data, scatter_kws={'s':50}, line_kws={"color":"red"})
plt.title('Total Medals vs Social Support')
plt.xlabel('Social Support')
plt.ylabel('Total Medals')
plt.show()

# Visualization 4: Total Medals vs Healthy Life Expectancy
plt.figure(figsize=(8, 6))
sns.regplot(x='Explained by: Healthy life expectancy', y='total_medals', data=correlation_data, scatter_kws={'s':50}, line_kws={"color":"red"})
plt.title('Total Medals vs Healthy Life Expectancy')
plt.xlabel('Healthy Life Expectancy')
plt.ylabel('Total Medals')
plt.show()

# Visualization 5: Total Medals vs Perceptions of Corruption
plt.figure(figsize=(8, 6))
sns.regplot(x='Explained by: Perceptions of corruption', y='total_medals', data=correlation_data, scatter_kws={'s':50}, line_kws={"color":"red"})
plt.title('Total Medals vs Perceptions of Corruption')
plt.xlabel('Perceptions of Corruption')
plt.ylabel('Total Medals')
plt.show()
