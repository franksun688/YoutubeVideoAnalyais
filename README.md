# YoutubeVideoAnalysis

Statistical analysis of Youtube search results for 'coronavirus' in early March 2020.

Author: Lingyou Pang, Ran Sun, Libin Feng

Date: March 2020

File structure:

~/code : code for web scraping and data analysis

~/rawdata : raw results from web scraping

~/data : cleaned data and results from data analysis

Main components:


1. Web scraping - 'youtube_scrape_2.py'

We focused on YouTube video search results of keyword ‘coronavirus’. Due to the worldwide outbreak of the COVID-19, we were interested in how people react to the epidemic in terms of video uploading, views, attitude and so on.

The YouTube search results generally include two level of webpages. The first level is a list of videos, with attributes including title, channel, views, upload time, video length, video description and video preview image. Once we follow the hyperlink and go to the second level of each individual video, we would have another set of attributes including, likes, dislikes, channel subscribers, number of comments and so on. This would bring us extra information about the user’s attitude and opinions towards the video. 

We would mainly look at text and numerical data for our analysis. Image and video processing would be a separate task that requires further exploration.

In the web scraping process, we mainly developed two level of automation. Due to the following challenges that we encountered when looking at the data.
1). YouTube search results is listed on the webpage using infinity scroll, meaning there is no page tag for us to directly modify. Therefore, in the bottom level of automation, we used the selenium web engine to help to automatically scroll towards the end of the search list. Only through this approach, we can obtain the full list of search results. Note the missing record will be dropped in the process for simplicity. 

2). YouTube video search results are dynamically changing. Every minute, there could be a new video uploaded and unsurprisingly features like number of views, likes and dislike will increase over time. So we designed a top level of automation that can perform the search process every 3 hours (the time interval can be set as any other value based on user preferences).

The outcome from the web scraping would include a list of csv files that reflect the search results for each search process. 

The rest of the documentation along with visualization will be included in the individual notebook files.

2.Data cleaning and NLP - 'Video_cleaning.ipynb'

3.EDA - 'EDA.ipynb'

4.Model Statistical Analysis - 'Models.ipynb'

5.Conclusion

This project concentrates on the analysis of YouTube video data collected under the searching key word: coronavirus, we try to figure out the variation of people’s attention and what the most of audiences care about this current coronavirus situation. 

We started with raw data scraping and an automatic scraping pipeline is constructed, during which we solved the problem of infinite scrolling by designing our own engine. Then we conducted NLP and data cleaning. It followed by exploratory data analysis, which includes visualization of trending over different time point, word cloud clustering and some statistical summaries. After that, we built some machine learning and statistical models to take a deeper look into this data set and the method we used are linear regression, PCA, classification, clustering and sentimental analysis. 

During this process, there are indeed some interesting discoveries. We conclude that people firstly focused on what is going on in China, while recently they pay more attention to the action of the precedent and domestic situation with the increasing severity. Secondly, we conclude that linear model in predicting future viewers doesn’t work properly while PCA successfully reduced the dimensionality to three and text classification model could accurately predict that if a video with certain features or key words will become likeable or not in the future. The sentimental analysis indicates that people generally feed depressed about this whole condition and even the news title express severely negative feelings. We also find that the video length approximately fellows a Pearson Type 3 distribution.

The limitation of this project is the limited numbers of observations since for each scraping the resulting number of videos is only around 400, which can be a little bit problematic and may yield biased results. One possible solution we want to try in the future is to try some different searching key words or use other website as source. The strengths are the fluently function of our scraping pipeline and diversity of the different model.



