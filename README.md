# The Happiness-Medal Nexus: Exploring Well-being and Olympic Success
## country_happiness_medal


This project started in September 2024 as a passion-driven initiative fueled by a love for data analysis and continuous learning. It leverages open-source datasets, with full attribution given to the original creators. Any modifications made to the data, such as cleansing, wrangling, and normalization, are purely for analytical purposes.
## 📖 Step-by-Step Usage Guide  
<!-- by 植美霞 -->

### 1. Data Preparation  
- **Download datasets**:  
  - [World Happiness Report](https://worldhappiness.report/)  
  - [Olympic Medal Data](https://olympics.com/en/paris-2024/medals)  
- **File structure**:  
![data_structure](images/2205308070351_01.jpg)  
<!-- by 植美霞 -->

### 2. Running the Analysis  
#### Correlation Analysis (Python Example)  
```python
import pandas as pd
# Load data
happiness = pd.read_csv("data/happiness.csv")  
medals = pd.read_csv("data/medals.csv")  
# Merge datasets
merged = pd.merge(happiness, medals, on="Country")  
# Calculate correlation
print(merged[["Happiness Score", "Total Medals"]].corr())


The dataset brings together insights from the World Happiness Report (WHR), Olympic medal counts, and various happiness score components (such as GDP, social support, and more). The aim is to explore five key analyses, particularly focusing on the relationship between national happiness and Olympic success:
1. Correlation Between Total Medals and Happiness Scores: Investigate whether countries that win more Olympic medals also tend to have higher happiness ladder scores in the WHR.

2. Economic Prosperity (Log GDP per Capita) and Olympic Performance: Explore if wealthier countries, as indicated by GDP per capita, are more successful in the Olympics.

3. Social Support and Olympic Success: Assess whether countries with stronger social support systems, as reflected in the WHR, tend to perform better in the Olympics.

4. Healthy Life Expectancy and Medal Counts: Analyze whether nations with higher life expectancies—often a sign of a healthier population—have greater Olympic success.

5. Perceptions of Corruption and Olympic Performance: Examine if lower levels of perceived corruption are linked to higher medal counts, potentially reflecting systemic factors that influence sports achievement.

6. Country and Regional Deep Dives: Provide detailed insights into individual countries and regions, offering a more granular exploration of happiness and sports performance.

*** See the full project and expanded insights over time will appear here: (https://brianfperry.com/landing/country_happiness_medal/)

*** See corresponding code in accompanying repo folder (https://github.com/dcrefugee/country_happiness_medal/blob/main/_code_happiness_medal_2024/load_and_explore.py)

---

Data Sources:  
- World Happiness Report: https://worldhappiness.report/  
- Olympic Medals - Paris 2024: https://olympics.com/en/paris-2024/medals
