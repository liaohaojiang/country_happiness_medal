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

###########
###########

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

#################################
#################################

### Identifying outliers by looking at large differences between expected happiness and actual medal counts.
### Here we calculate the z-scores for both Ladder score and total medals and identify countries with the largest absolute differences between the two.

from scipy.stats import zscore

# Calculating z-scores for total medals and Ladder score
df['z_medals'] = zscore(df['total_medals'])
df['z_ladder_score'] = zscore(df['Ladder score'])

# Calculating the absolute difference between z-scores of total medals and Ladder score
df['z_diff'] = abs(df['z_medals'] - df['z_ladder_score'])

# Sort by the largest absolute z-score differences
outliers_large_z_diff = df.sort_values(by='z_diff', ascending=False).head(10)

# Display the top 10 outliers
outliers_large_z_diff[['country', 'total_medals', 'Ladder score', 'z_medals', 'z_ladder_score', 'z_diff']]

### Other possible metrics such as Log GDP per capita, Social support, and Healthy life expectancy

# List of metrics to explore
metrics = ['Explained by: Log GDP per capita', 'Explained by: Social support', 'Explained by: Healthy life expectancy']

# Correlations between these metrics and total medals
correlation_results = df[['total_medals'] + metrics].corr()

# Extracting correlations of the metrics with total medals for insights
correlation_with_medals = correlation_results['total_medals'].drop('total_medals')

# Sort correlations by absolute value to find the strongest relationships
sorted_correlations = correlation_with_medals.abs().sort_values(ascending=False)

# Display the correlation results
sorted_correlations

#####################
#####################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example DataFrame (please replace with your actual 'df' data)
# df should contain at least the following columns: 'country', 'Explained by: Log GDP per capita', 'total_medals', 'Explained by: Healthy life expectancy'
data = {
    'country': ['United States', 'China', 'Australia', 'Norway', 'Japan', 'Ethiopia', 'Botswana'],
    'Explained by: Log GDP per capita': [10.5, 9.5, 10.0, 11.0, 9.8, 8.2, 7.5],
    'total_medals': [121, 70, 30, 40, 41, 5, 3],
    'Explained by: Healthy life expectancy': [68, 72, 75, 80, 79, 50, 45]
}
df = pd.DataFrame(data)

# List of countries to highlight and assign a number to each country
highlighted_countries = ['United States', 'China', 'Australia', 'Norway', 'Japan', 'Ethiopia', 'Botswana']
country_numbers = {country: idx + 1 for idx, country in enumerate(highlighted_countries)}

# Create a DataFrame to display the country names and corresponding numbers
highlighted_df = pd.DataFrame(list(country_numbers.items()), columns=['Country', 'Number'])

# Function to plot the chart and the table side by side
def plot_with_table(x_col, y_col, title, x_label, y_label):
    # Set up the figure with a grid for the plot and the table
    fig = plt.figure(figsize=(12, 7))
    gs = fig.add_gridspec(1, 2, width_ratios=[3, 1], wspace=0.3)

    # Create the scatter plot with regression line
    ax = fig.add_subplot(gs[0])
    sns.regplot(x=x_col, y=y_col, data=df, scatter_kws={'s': 50}, line_kws={"color": "red"}, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Add larger and bolded number labels for selected countries
    for i, row in df.iterrows():
        if row['country'] in highlighted_countries:
            country_num = country_numbers[row['country']]
            ax.text(row[x_col], row[y_col], str(country_num), fontsize=12, fontweight='bold', 
                    verticalalignment='bottom', horizontalalignment='right')

    # Create a table on the right side of the plot
    ax_table = fig.add_subplot(gs[1])
    ax_table.axis('tight')
    ax_table.axis('off')

    # Render the country name-number table on the plot
    table_data = highlighted_df[['Number', 'Country']].sort_values('Number').values
    table = ax_table.table(cellText=table_data, colLabels=["Number", "Country"], cellLoc='center', loc='center')

    # Adjust the font size of the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.show()

# Visualization 1: Total Medals vs Log GDP per Capita
plot_with_table('Explained by: Log GDP per capita', 'total_medals', 
                'Total Medals vs Log GDP per Capita', 'Log GDP per Capita', 'Total Medals')

# Visualization 2: Total Medals vs Healthy Life Expectancy
plot_with_table('Explained by: Healthy life expectancy', 'total_medals', 
                'Total Medals vs Healthy Life Expectancy', 'Healthy Life Expectancy', 'Total Medals')

#########
#########

# Grouping the data by region and calculate the mean for only numeric columns
region_data = df.groupby('world_region').mean(numeric_only=True)[['total_medals', 'Ladder score', 
                                                                  'Explained by: Log GDP per capita',
                                                                  'Explained by: Social support', 
                                                                  'Explained by: Healthy life expectancy']]

# Reset index to turn the 'world_region' into a column if necessary
region_data = region_data.reset_index()

print(region_data)

#######
#######

# Focused analysis on North America and ANZ, and Western Europe

# Subset data for North America and ANZ, and Western Europe
na_anz_we = df[df['world_region'].isin(['North America and ANZ', 'Western Europe'])]

# Visualization 1: Comparison of medals, happiness, GDP, social support, and life expectancy
metrics = ['total_medals', 'Ladder score', 'Explained by: Log GDP per capita',
           'Explained by: Social support', 'Explained by: Healthy life expectancy']

# Set up the grid for the plots
plt.figure(figsize=(15, 10))

# Plot each metric
for i, metric in enumerate(metrics, 1):
    plt.subplot(3, 2, i)
    sns.barplot(x='world_region', y=metric, data=na_anz_we, palette="viridis")
    plt.title(f'{metric} Comparison: North America and ANZ vs Western Europe')
    plt.xlabel('World Region')
    plt.ylabel(metric)

plt.tight_layout()
plt.show()

####
####

# Subset data for Sub-Saharan Africa and South Asia
ssa_sa = df[df['world_region'].isin(['Sub-Saharan Africa', 'South Asia'])]

# Visualization: Comparison of medals, happiness, GDP, social support, and life expectancy for underperforming regions
plt.figure(figsize=(15, 10))

# Plot each metric for Sub-Saharan Africa and South Asia
for i, metric in enumerate(metrics, 1):
    plt.subplot(3, 2, i)
    sns.barplot(x='world_region', y=metric, data=ssa_sa, palette="magma")
    plt.title(f'{metric} Comparison: Sub-Saharan Africa vs South Asia')
    plt.xlabel('World Region')
    plt.ylabel(metric)

plt.tight_layout()
plt.show()

#####
#####

# Subset data for MENA, Latin America and Caribbean, and East Asia
mena_la_ea = df[df['world_region'].isin(['Middle East and North Africa', 'Latin America and Caribbean', 'East Asia'])]

# Visualization: Comparison of medals, happiness, GDP, social support, and life expectancy for these regions
plt.figure(figsize=(15, 10))

# Plot each metric for MENA, Latin America, and East Asia
for i, metric in enumerate(metrics, 1):
    plt.subplot(3, 2, i)
    sns.barplot(x='world_region', y=metric, data=mena_la_ea, palette="coolwarm")
    plt.title(f'{metric} Comparison: MENA vs Latin America vs East Asia')
    plt.xlabel('World Region')
    plt.ylabel(metric)

plt.tight_layout()
plt.show()

######
######

# Subset data for East Asia, Southeast Asia, and South Asia
asia_regions = df[df['world_region'].isin(['East Asia', 'Southeast Asia', 'South Asia'])]

# Visualization: Comparison of medals, happiness, GDP, social support, and life expectancy for Asian regions
plt.figure(figsize=(15, 10))

# Plot each metric for East Asia, Southeast Asia, and South Asia
for i, metric in enumerate(metrics, 1):
    plt.subplot(3, 2, i)
    sns.barplot(x='world_region', y=metric, data=asia_regions, palette="RdYlBu")
    plt.title(f'{metric} Comparison: East Asia vs Southeast Asia vs South Asia')
    plt.xlabel('World Region')
    plt.ylabel(metric)

plt.tight_layout()
plt.show()

#######
#######

# Subset data for Sub-Saharan Africa to explore its challenges
africa_region = df[df['world_region'] == 'Sub-Saharan Africa']

# Visualization: Comparison of medals, happiness, GDP, social support, and life expectancy for Sub-Saharan Africa
plt.figure(figsize=(15, 8))

# Plot each metric for Sub-Saharan Africa
for i, metric in enumerate(metrics, 1):
    plt.subplot(3, 2, i)
    sns.barplot(x='country', y=metric, data=africa_region, palette="magma")
    plt.title(f'{metric} for Sub-Saharan Africa')
    plt.xlabel('Country')
    plt.ylabel(metric)
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#####
#####
