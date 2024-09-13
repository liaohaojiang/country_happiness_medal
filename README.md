# The Happiness-Medal Nexus: Exploring Well-being and Olympic Success
## country_happiness_medal

This project started in September 2024 as a passion-driven initiative fueled by a love for data analysis and continuous learning. It leverages open-source datasets, with full attribution given to the original creators. Any modifications made to the data, such as cleansing, wrangling, and normalization, are purely for analytical purposes.

The dataset brings together insights from the World Happiness Report (WHR), Olympic medal counts, and various happiness score components (such as GDP, social support, and more). The aim is to explore five key analyses, particularly focusing on the relationship between national happiness and Olympic success:

1. Correlation Between Total Medals and Happiness Scores: Investigate whether countries that win more Olympic medals also tend to have higher happiness ladder scores in the WHR.

2. Economic Prosperity (Log GDP per Capita) and Olympic Performance: Explore if wealthier countries, as indicated by GDP per capita, are more successful in the Olympics.

3. Social Support and Olympic Success: Assess whether countries with stronger social support systems, as reflected in the WHR, tend to perform better in the Olympics.

4. Healthy Life Expectancy and Medal Counts: Analyze whether nations with higher life expectancies—often a sign of a healthier population—have greater Olympic success.

5. Perceptions of Corruption and Olympic Performance: Examine if lower levels of perceived corruption are linked to higher medal counts, potentially reflecting systemic factors that influence sports achievement.

6. Country and Regional Deep Dives: Provide detailed insights into individual countries and regions, offering a more granular exploration of happiness and sports performance.

## 13 September 2024

See corresponding code in accompanying repo folder (https://github.com/dcrefugee/country_happiness_medal/blob/main/_code_happiness_medal_2024/load_and_explore.py)

Key insights based on the correlation matrix:

- Total Medals and Happiness Scores (Ladder Score): There is a moderate positive correlation (0.255) between total medals won and a country's happiness score. This suggests that countries with higher happiness levels may also experience greater success in the Olympics, though the relationship is not very strong.

- GDP and Medal Success: The correlation between total medals and GDP per capita is 0.31, indicating that wealthier countries tend to win more Olympic medals. However, the correlation isn't very high, meaning there are other important factors at play.

- Social Support and Olympic Performance: There is a weaker positive correlation (0.19) between social support and total medals won, showing that higher social support does not strongly translate into Olympic success, though it may still have some influence.

- Healthy Life Expectancy and Medal Counts: A correlation of 0.21 suggests a slight link between higher life expectancy and Olympic success. Healthier nations may have a small advantage in Olympic sports, but it's not a decisive factor on its own.

- Corruption and Medal Success: The correlation between perceived corruption and total medals is 0.21. Countries with lower corruption tend to perform slightly better in the Olympics, but the effect is not particularly strong.

The next chart below is the Total Medals vs Ladder Score (Happiness) chart with select highlighted countries: United States, China, Australia, Norway, and Japan. 

These countries show some interesting trends in both happiness scores and Olympic success.

Expanded Insights: United States:

High medal count and relatively high happiness score. Reflects the balance between economic prosperity, sports infrastructure, and societal well-being contributing to Olympic success. China:

Strong Olympic performance, but the happiness score is lower than the United States. This demonstrates that high medal counts are not always tied to societal happiness but can be the result of targeted sports programs and government investment. Australia:

High happiness score and a substantial number of medals. A good example of how countries with high levels of happiness can also perform well at the Olympics, likely due to strong social systems and investments in sports. Norway:

Small population but high medal count relative to size, combined with one of the highest happiness scores. Indicates that smaller, happier nations with strong health and sports programs can perform disproportionately well in international sports. Japan:

A moderate number of medals and relatively high happiness, though not at the level of the U.S. or China in terms of total medals. Suggests that happiness is a factor, but not the primary one in driving sports success. These insights show that while there is a positive relationship between happiness and Olympic success, it is not the sole determining factor, with economic and structural investments playing a significant role.


This project will continue to evolve over time, with new findings and updates shared periodically.

---

Data Sources:  
- World Happiness Report: https://worldhappiness.report/  
- Olympic Medals - Paris 2024: https://olympics.com/en/paris-2024/medals
