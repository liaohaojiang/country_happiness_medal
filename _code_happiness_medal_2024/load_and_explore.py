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

###Total Medals vs Ladder Score (Happiness) chart with select highlighted countries: United States, China, Australia, Norway, and Japan. These countries show some interesting trends in both happiness scores and Olympic success.

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plot
sns.set(style="whitegrid")

# Create a plot for Total Medals vs Ladder Score (Happiness)
plt.figure(figsize=(10, 7))
sns.regplot(x='Ladder score', y='total_medals', data=df, scatter_kws={'s':50}, line_kws={"color":"red"})
plt.title('Total Medals vs Ladder Score (Happiness)')
plt.xlabel('Ladder Score (Happiness)')
plt.ylabel('Total Medals')

# Highlighting selected countries with numbers for more insights
highlighted_countries = ['United States', 'China', 'Australia', 'Norway', 'Japan']
country_mapping = {1: 'United States', 2: 'China', 3: 'Australia', 4: 'Norway', 5: 'Japan'}

# Loop through the DataFrame and label the countries by number
for i, row in df.iterrows():
    if row['country'] in highlighted_countries:
        # Get the corresponding number for each country
        country_number = [key for key, value in country_mapping.items() if value == row['country']][0]

        # Check if the row corresponds to the United States and annotate properly
        if row['country'] == 'United States' and row['Ladder score'] == 6.725 and row['total_medals'] == 126:
            plt.annotate(str(country_number), xy=(row['Ladder score'], row['total_medals']),
                         xytext=(row['Ladder score'] + 0.3, row['total_medals'] + 10), 
                         fontsize=12, arrowprops=dict(facecolor='black', arrowstyle='->'))
        else:
            # For other countries, use regular text positioning
            plt.text(row['Ladder score'], row['total_medals'], str(country_number), 
                     fontsize=10, verticalalignment='bottom', horizontalalignment='right')

# Ensure the plot limits are adequate to display all data points and labels
plt.xlim(df['Ladder score'].min() - 0.5, df['Ladder score'].max() + 0.5)
plt.ylim(df['total_medals'].min() - 10, df['total_medals'].max() + 20)

# Create the legend for the numbers
legend_labels = [f"{num}. {country}" for num, country in country_mapping.items()]
legend_text = "\n".join(legend_labels)

# Position the legend to the right of the plot
plt.text(1.05, 0.5, legend_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='center', bbox=dict(facecolor='white', edgecolor='black'))

# Display the plot
plt.show()
