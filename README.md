# ProjectMatchr
Insight Data Science fellowship project

## Background
The demand for data scientists remains high across a wide variety of industries, and there are ample resources for aspiring data scientists to acquire the skills and experience needed to be competitive for these jobs. With the vast availability of resources, there are many publicly available data sets that have been overused and project ideas that have been overdone, making it hard to stand out or come up with novel ways to demonstrate one's data science capabilities.

To this end, ProjectMatchr is a tool to help data scientists brainstorm viable project ideas by seeing what's been done before. 

## How ProjectMatchr Works
On the ProjectMatchr web application, the user inputs keywords related to their data science project idea. In this version, the user can only select one action verb that describes the project's purpose (e.g., "recommend"), as well as one topic (e.g., "recipe"). ProjectMatchr returns previous projects that are most similar to the keywords entered. Where available, the app will provide links to additional project resources, such as a github repository or a presentation describing the project methodology. These resources are designed to help the user understand the data science techniques and tools needed to complete a similar project. 

![projmatchr_screenshot](https://user-images.githubusercontent.com/7207786/41804599-7a58121c-7667-11e8-98ab-d18e6820d76e.jpg)

## On the Back End
To complete this project, I scraped data from two data science career accelerator program websites using Python's Beautiful Soup library. My dataset includes information on program participants such as their name, degree, academic background, hiring company, and project title. Using only the project title data, 

## Interesting Findings
![nlp_freq_chart](https://user-images.githubusercontent.com/7207786/41804676-aeb2ae72-7668-11e8-950c-640dc4c43150.png)

