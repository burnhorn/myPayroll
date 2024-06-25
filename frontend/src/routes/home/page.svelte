<main>
  <h1>Project Overview</h1>
  <section>
      <h1>1. Issue</h1>
      <p>Through this project, I aim to enhance my programming skills and leverage data to derive valuable insights. By utilizing FastAPI and Svelte, I have developed a website that ranges from simple salary calculations to comprehensive dashboard presentations using slide functionalities. This project showcases my knowledge in HR, data management, and basic IT skills.</p>
  </section>

  <section>
      <h1>2. Approach Method</h1>
      <p>I aim to distinguish between data and information. This project explains the process of how raw data is transformed into meaningful information through processing. The focus is on refining raw data based on context, relevance, and purpose to produce valuable information. This approach is intended to improve the reliability of data and enhance my ability to provide valuable insights.</p>
  </section>

  <section>
      <h1>3. Skills</h1>
      <h2>(1) Technologies and Tools Used</h2>
      <ul>
          <li>Python</li>
          <li>FastAPI</li>
          <li>Svelte</li>
          <li>Pandas</li>
          <li>Google Cloud Platform (GCP)</li>
          <li>PostgreSQL</li>
      </ul>

      <h2>(2) The reason for Tool Selection</h2>
      <ul>
          <li>Low Learning Curve for Fast Builds: Selected tools that enable rapid development and are easy to learn.</li>
          <li>Cloud-Based Technology Familiarity: Utilized GCP to gain familiarity with cloud-based technologies.</li>
          <li>Stable Data Management: Chose PostgreSQL for reliable and robust data management.</li>
      </ul>
  </section>

  <section>
      <h1>4. Project link</h1>
      <p>You can find all my projects here:</p>
      <a href="https://youhave.store/" target="_blank">https://youhave.store/</a>
  </section>

  <section>
      <h1>5. First example of my project</h1>
      <img src="https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/basic.PNG "alt="Basic Dashboard Example" />
      <p>The above image shows a dashboard created by using the pivot table and slicer function of Excel from data processed by Pandas.</p>
  </section>

  <section>
      <h1>6. Second example of my project</h1>
      <pre><code>{`
# Scraping
url = 'Searching Site URL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'xml.parser')

# choose css selector
title_soup = soup.select('ccs.tag')
titles = [title.text for title in title_soup]

# create dataframe
df = pd.DataFrame("title" : titles)

text_data = df['title'].dropna()

def extract_nouns(text):
  nouns = re.findall(r'\\b[가-힣]+\\b', text)
  return nouns

# Extract nouns from all text data
all_nouns = []
for text in text_data:
  all_nouns.extend(extract_nouns(text))

noun_counts = Counter(all_nouns)
      `}</code></pre>
      <p>Running the program we get the following output:</p>
      <img src="https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/scraper.png" alt="Scraper Output Example" />
      <p>The above image shows searching data("가상화폐") collected using requests and BeautifulSoup, and visualized using WordCloud.</p>
  </section>

  <section>
      <h1>4. Result</h1>
      <p>Previously, collecting, organizing, and processing data to produce meaningful information required significant time and effort. This project highlights the efficiency gains achieved through advanced IT technologies and programming languages like Python. By automating these processes, I was able to focus my limited resources (time, attention, etc.) on high-value tasks. The ability to quickly adapt to and effectively utilize new tools is a critical mindset in the era of the Fourth Industrial Revolution.</p>
  </section>

  <section>
      <h1>Summary</h1>
      <p>This project serves as a testament to my proactive approach to learning and my commitment to using data-driven methods to generate value. It underscores the importance of both technical proficiency and the ability to derive actionable insights from data.</p>
  </section>
</main>

<style>
  main {
      font-family: Arial, sans-serif;
      line-height: 1.6;
  }

  section {
      margin-bottom: 2em;
  }

  h1, h2 {
      color: #333;
  }

  ul {
      list-style-type: disc;
      margin-left: 20px;
  }

  a {
      color: #007BFF;
      text-decoration: none;
  }

  a:hover {
      text-decoration: underline;
  }

  pre {
      background-color: #f4f4f4;
      padding: 10px;
      border-radius: 5px;
      overflow-x: auto;
  }

  img {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
  }
</style>
