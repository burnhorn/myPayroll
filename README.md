# 1. Issue

Through this project, I aim to enhance my programming skills and leverage data to derive valuable insights. By utilizing FastAPI and Svelte, I have developed a website that ranges from simple salary calculations to comprehensive dashboard presentations using slide functionalities. This project showcases my knowledge in HR, data management, and basic IT skills.

# 2. Approach Method

I aim to distinguish between data and information. This project explains the process of how raw data is transformed into meaningful information through processing. The focus is on refining raw data based on context, relevance, and purpose to produce valuable information. This approach is intended to improve the reliability of data and enhance my ability to provide valuable insights.

# 3. Skills

**(1) Technologies and Tools Used**

![Reference Image](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Reference Image](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Reference Image](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Reference Image](https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white)
![Reference Image](https://img.shields.io/badge/GoogleCloud-4285F4?style=for-the-badge&logo=google%cloud&logoColor=white)
![Reference Image](https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

**(2) The reason for Tool Selection**

    - Low Learning Curve for Fast Builds: Selected tools that enable rapid development and are easy to learn.
    - Cloud-Based Technology Familiarity: Utilized GCP to gain familiarity with cloud-based technologies.
    - Stable Data Management: Chose PostgreSQL for reliable and robust data management.

# 4. Project link

you can find all my project's here :
[https://youhave.store/](https://youhave.store/)

# 5. First example of my project

![Reference Image](https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/basic.PNG)

`The above image shows a dashboard created by using the pivot table and slicer function of Excel from data processed by Pandas.`

# 6. Second example of my project

For main code

```python

# Scraping
url = 'Searching Site URL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'xml.parser')

# choose css tag
title_soup = soup.select('ccs.tag')
titles = [title.text for title in title_soup]

# create dataframe
df = pd.DataFrame("title" : titles)

text_data = df['title'].dropna()

def extract_nouns(text):
    nouns = re.findall(r'\b[가-힣]+\b', text)
    return nouns

# Extract nouns from all text data
all_nouns = []
for text in text_data:
    all_nouns.extend(extract_nouns(text))

noun_counts = Counter(all_nouns)
```

**Running the program we get the following output**

![Reference Image](https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/scraper.png)

`The above image shows searching data("가상화폐") collected using requests and BeautifulSoup, and visualized using WordCloud.`

# 7. Result

Previously, collecting, organizing, and processing data to produce meaningful information required significant time and effort. This project highlights the efficiency gains achieved through advanced IT technologies and programming languages like Python. By automating these processes, I was able to focus my limited resources (time, attention, etc.) on high-value tasks. The ability to quickly adapt to and effectively utilize new tools is a critical mindset in the era of the Fourth Industrial Revolution.

# 8. Summary

This project serves as a testament to my proactive approach to learning and my commitment to using data-driven methods to generate value. It underscores the importance of both technical proficiency and the ability to derive actionable insights from data.
