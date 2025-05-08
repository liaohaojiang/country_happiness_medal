

# 幸福与奖牌的联系：探索幸福与奥运成功
##国家幸福与奥运奖牌项目

该项目于 2024 年 9 月启动，是一项充满激情的倡议，由对数据分析和持续学习的热爱推动。它利用开源数据集，并完全归属于原始创作者。对数据所做的任何修改（例如清理、整理和规范化）仅用于分析目的。

该数据集汇集了来自世界幸福报告（WHR）、奥运会奖牌数和各种幸福感分数组成部分（如 GDP、社会支持等）的见解。目的是探索五个关键分析，特别关注国家幸福感与奥林匹克成功之间的关系：

1. 总奖牌数与幸福感分数之间的相关性：调查赢得更多奥运奖牌的国家是否也往往在 WHR 中具有更高的幸福感阶梯分数。
2. 经济繁荣（人均 GDP 对数）和奥林匹克表现：探索较富裕的国家（以人均 GDP 表示）是否在奥运会上更成功。
3. 社会支持和奥林匹克成功：评估 WHR 所反映的具有更强大社会支持系统的国家是否倾向于在奥运会上表现更好。
4.健康预期寿命和奖牌数：分析预期寿命较高的国家（通常是人口健康的标志）是否在奥运会上取得更大的成功。
5. 对腐败和奥林匹克表现的看法：检查较低水平的感知腐败是否与较高的奖牌数有关，这可能反映了影响体育成就的系统性因素。

6. 国家和地区深入研究：提供对各个国家和地区的详细见解，提供更精细的幸福感和运动表现探索。
*** 查看完整项目，随着时间的推移，扩展的见解将在此处显示：
(https://brianfperry.com/landing/country_happiness Medal/)

*** 请参阅随附的 repo 文件夹 (https://github.com/dcrefugee/country_happiness_medal/blob/main/_code_happiness_medal_2024/load_and_explore.py)

---











































































数据来源：
- 世界幸福报告：https://worldhappiness.report/  
- 奥运会奖牌 - 2024年巴黎奥运会：https://olympics.com/en/paris-2024/medals
输入：<!-- by 廖浩江 -->
输入：- 安装 / 部署说明部分内容：

### 安装和部署

#### 系统要求
- **操作系统**：Windows 10 或更高版本，macOS 10.15 或更高版本，Linux（推荐 Ubuntu 20.04 或更高版本）。
- **Python 版本**：Python 3.8 或更高版本。
- **内存**：至少2GB RAM。
- **存储**：至少有500MB的可用磁盘空间。

#### 安装步骤

1. **克隆仓库**
首先，使用以下命令将项目代码库克隆到你的本地机器：
```bash
git 克隆 https://github.com/liaohaojiang/country_happiness Medal.git
cd 国家幸福奖章

This will create a local copy of the repository in your current working directory.
2. Navigate to the Project Directory: After cloning, use the cd command to enter the project directory:
bash
cd country_happiness_medal
Create a Virtual Environment (Optional but Recommended): It is good practice to use a virtual environment to isolate the project's dependencies. On Windows, you can use the following commands:
bash
python -m venv myenv
myenv\Scripts\activate
On macOS and Linux:
bash
python3 -m venv myenv
source myenv/bin/activate
Install Dependencies: With the virtual environment activated (if you chose to use one), install the required Python libraries. You can use pip to install them. Create a requirements.txt file in the project directory with the following content:
plaintext
pandas
numpy
seaborn
scikit - learn
Then run the command:
bash
pip install -r requirements.txt
This will install all the necessary libraries for the project.
Configuration Methods
Data Sources: The project uses data from the World Happiness Report and the 2024 Paris Olympics medal data. Ensure that the data files (2024 Medal and WHR Master Table.csv, 2024 WHR and Medal Country outliers_large_z_diff.csv, 2024_medal_ladder_z_by_region.csv) are present in the project directory. If you want to update the data, you can download the latest versions from the official sources (https://worldhappiness.report/ and https://olympics.com/en/paris - 2024/medals) and replace the existing files.
Code Configuration: If you need to modify the analysis code in the _code_happiness_medal_2024 folder, make sure you understand the functionality of each module. For example, if you want to change the statistical methods used in the correlation analysis in load_and_explore.py, you should carefully review the code and the relevant documentation of the libraries being used.



输入：=======
# 项目介绍

## 背景










2024年9月，“幸福-奖牌联系：探索幸福与奥运成功”项目在对数据分析的深厚热情和对持续学习的坚定承诺下启动。在一个数据能够揭示复杂关系的世界里，我们对国家幸福与奥运表现之间潜在联系感到好奇。

我们获取了开源数据集，并充分感谢原始创作者。所有数据预处理步骤，例如清理以消除错误和不一致性、整理以将数据转换为适当格式、以及标准化以统一值，都是为了进行深入和准确的分析而严格进行的。

## 目的










这个项目的核心目标是全面探索国家幸福与奥运成就之间的关系。通过整合《世界幸福报告》（WHR）、奥运奖牌数以及幸福指数的各个组成部分，包括GDP、社会支持等数据，我们旨在进行五项关键分析。这些分析旨在揭示国家幸福相关的因素，如幸福、经济繁荣、社会支持、预期寿命和腐败感知等，是否对国家的奥运表现有显著影响。

## 功能

### 相关性分析
我们进行统计调查，以确定一个国家赢得的奥运奖牌总数与其在世界幸福报告中的幸福指数之间的相关性。此分析帮助我们了解是否存在一种普遍趋势，即奥运表现更出色的国家往往拥有更高的国民幸福水平。

### 经济影响探索
我们探讨了一个国家的经济繁荣（通过人均GDP的对数衡量）与在奥运会上的表现之间的关系。人均GDP较高通常意味着更好的体育基础设施、运动员训练和发展项目资源。此分析旨在揭示富裕国家在奥运比赛中是否具有竞争优势。

### 社会支持评估
我们评估国家的社会支持系统（在《世界幸福报告》中反映出来）如何影响其奥运表现。一个强大的社会支持系统可以为运动员提供必要的情感、财务和制度支持。通过分析这种关系，我们可以了解是否拥有更强大社会支持网络的国家更有可能培养出成功的奥运运动员。

###健康预期寿命分析
通过研究一个国家的健康预期寿命与奖牌数量之间的关系，我们旨在了解一个更健康的劳动力是否有助于在奥运会上取得更大的成功。更高的预期寿命通常是一个运作良好的医疗系统、健康的生活方式和总体良好生活条件的指标，这些都可能对运动员有益。

### 腐败感知调查
我们研究了感知到的腐败水平较低与奖牌数量较多之间的联系。腐败可能会破坏体育比赛的公平性，限制运动员获取资源的机会，并扰乱体育机构的正常运作。此分析可以突出可能影响体育成就的系统性因素，以及对奥运会成功而言，保持无腐败环境的重要性。

### 国家和区域洞察
我们对各个国家和地区的详细情况提供了见解。这使得我们可以更细致地探索幸福与运动表现之间的关系，同时考虑到每个国家或地区的独特文化、社会和经济特征。

## 功能
- **数据驱动方法**：该项目 firmly基于来自可靠来源的现实世界数据。这确保了我们分析的客观性和可信性，使我们能够基于实证证据得出有意义的结论。
- **Multifaceted Analysis**: By considering multiple factors related to national well - being and Olympic performance, we offer a comprehensive view of the relationship between the two. This holistic approach helps us capture the complex interplay of various elements that contribute to a country's Olympic success.
- **Open - Source and Transparent**: We use open - source datasets and make our code publicly available. This promotes transparency in our research process and allows other researchers to reproduce our results, validate our findings, and build upon our work.

=======
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

