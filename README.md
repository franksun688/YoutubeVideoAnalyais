# YoutubeVideoAnalyais

Statistical analysis of Youtube search results for 'coronavirus' in early March 2020.

Author: Lingyou Pang, Ran Sun, Libin Feng

Date: March 2020

File structure:

~/code : code for web scraping and data analysis

~/rawdata : raw results from web scraping

~/data : cleaned data and results from data analysis


Introduction:

Due to the outbreak of the Coronavirus, people over the globe are eagered to accuire information from all possible media portals. YouTube is a substitute when cable is not installed. Many videos are uploaded or streamed since the beginning of the year 2020. In order to attract the audience, uploaders may have named their videos in some way that is easily to be searched or more likely to be clicked by users. We were interested in how people react to the epidemic in terms of video uploading, views, attitude and so on.



Main components:

1. Web scraping (youtube_scrape_2.py)

We focused on YouTube video search results of key word ‘coronavirus’. Using BeautifulSoup html scraper and chrome engine, we extracted data from the search result starting around March 10. 

The YouTube search results generally include two level of webpages. The first level is a list of videos, with attributes including title, channel, views, upload time, video length, video description and video preview image. Once we follow the hyperlink and go to the second level of each individual video, we would have another set of attributes including, likes, dislikes, channel subscribers, number of comments and so on. This would bring us extra information about the user’s attitude and opinions towards the video. 

We would mainly look at text and numerical data for our analysis. Image and video processing would be a separate task that requires further exploration.

In the web scraping process, we mainly developed two level of automation. Due to the following challenges that we encountered when looking at the data.

1). YouTube search results is listed on the webpage using infinity scroll, meaning there is no page tag for us to directly modify. Therefore, in the bottom level of automation, we used the selenium web engine to help to automatically scroll towards the end of the search list. Only through this approach, we can obtain the full list of search results. Note the missing record will be dropped in the process for simplicity. 

2). YouTube video search results are dynamically changing. Every minute, there could be a new video uploaded and unsurprisingly features like number of views, likes and dislike will increase over time. Since the event is evolving and has frequent updates, we designed a top level of automation that can perform the search process every 3 hours (the time interval can be set as any other value based on user preferences).

The outcome from the web scraping would include a list of csv files that reflect the search results for each search process. 

The rest of the documentation along with visualization will be included in the individual notebook files.

2. Data cleaning (Video_NLP - corrected.ipynb)

3. Exploratory Data Analysis (EDA.ipynb)

4. Statistical Analysis (Models.ipynb)

5. Conclusion