# ProjectMatchr
<a href="http://insightdatascience.com"> Insight Data Science </a> fellowship project

<a href="http://projectmatchr.io">projectmatchr.io</a>

## Background
The demand for data scientists remains high across a wide variety of industries, and there are ample resources for aspiring data scientists to acquire the skills and experience needed to be competitive for these jobs. With the vast availability of resources, there are many publicly available data sets that have been overused and project ideas that have been overdone, making it hard to stand out or come up with novel ways to demonstrate one's data science capabilities.

To this end, ProjectMatchr is a tool to help data scientists brainstorm viable project ideas by seeing what's been done before and where there may be opportunities for a unique project idea. 

## How ProjectMatchr Works
On the ProjectMatchr web application, the user inputs keywords related to their data science project idea. In the current version of the application, the user can only select one action verb that describes the project's purpose (e.g., "recommend"), as well as one topic (e.g., "food/drink"). ProjectMatchr returns previous projects that are most similar to the keywords entered. Where available, the app will provide links to additional project resources, such as a github repository or a presentation describing the project methodology. These resources are designed to help the user understand the data science techniques and tools needed to complete a similar project with their own unique spin. 

![projmatchr_screenshot](https://user-images.githubusercontent.com/7207786/41804599-7a58121c-7667-11e8-98ab-d18e6820d76e.jpg)

## On the Back End
To complete this project, I scraped data made available from two data science career accelerator program websites using Python's Beautiful Soup library. My structured dataset includes information on program participants such as their name, degree, academic background, hiring company, and project title. Only project title text is used, and is transformed using Python's Natural Language ToolKit (nltk module) into cleaned text tokens. Each project was hand labeled with informative keywords; keywords were validated using additional text from articles scraped from two data science blogs related to data science project ideation. This application matches user keyword input to project titles using a cosine similarity score from a pre-trained word2Vec model; up to five projects exceeding a particular score are returned. Where there are few to no matches, the application indicates that the user's choice of keywords may be an opportunity to create an innovative project.

Data scraping, wrangling, and modeling were completed using the following Python 2.7 modules: BeautifulSoup4, nltk, gensim, scikit-learn. The web application was built incorporating Flask and SQLAlchemy/PostgreSQL. 


## Interesting Findings
In many cases, project titles were still informative when boiled down to two parts of speech - a verb and a noun (e.g., map crime, find books). The chart below displays the frequency of words from project titles, and reveals that projects that "find", "recommend", or "predict" were the most common. Top topics of interest included "news", "social media", and "food/drink/restaurants".
![nlp_freq_chart](https://user-images.githubusercontent.com/7207786/41804676-aeb2ae72-7668-11e8-950c-640dc4c43150.png)

<a href="http://bit.ly/2Ix4Dfk"> Learn more </a>
