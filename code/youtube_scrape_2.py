#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:44:41 2020

@author: ransun

"""

# import packages
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time
import datetime
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# =============================================================================
#     load selenium  web deiver for automatic scroll
# =============================================================================
def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
        
# =============================================================================
# start webdriver
# =============================================================================
#url = "https://www.youtube.com/results?search_query=coronavirus"
def YT_scrape (url = 'https://www.youtube.com/results?search_query=coronavirus&sp=EgIQAQ%253D%253D'):
    '''option to make driver work background'''
#    chrome_options = Options()
#    chrome_options.add_argument('--headless')
#    chrome_options.add_argument('--disable-gpu')
    
    #driver = webdriver.Chrome('/usr/local/bin/chromedriver',options = chrome_options) 
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    #driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')  # firefox webdriver version
    
    
    driver.get(url)
    print('engine started')
    scroll(driver, 3)
    
    # Once scroll returns bs4 parsers the page_source
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    # Them we close the driver as soup_a is storing the page source
    driver.close()
    print('engine closed')
    # =============================================================================
    # beautiful soup parsing
    # =============================================================================
    # write the soup object to html first to be safe
#    with open("output1.html", "w", encoding='utf-8') as file:
#        file.write(str(soup))
    
        
    # =============================================================================
    #     retrive information
    # =============================================================================  
    videos = soup.find_all('ytd-video-renderer',attrs={'class':"style-scope ytd-item-section-renderer"},recursive=True)
    video_df = pd.DataFrame(np.zeros((len(videos),9)),columns = ['title', 'view', 'channel','uploadtime','length','link','subscriber','like','dislike'])
    
    count = 0
    err = 0
    for video in videos:
    
        try:
            title = video.find("yt-formatted-string", attrs={"class": "style-scope ytd-video-renderer"}).text.strip()
        
            view = video.find_all("span", attrs={"class": "style-scope ytd-video-meta-block"})[0].text.strip()
            
            channel = video.find_all('a',attrs={"class": "yt-simple-endpoint style-scope yt-formatted-string"})[0].text.strip()
            
            uploadtime = video.find_all("span", attrs={"class": "style-scope ytd-video-meta-block"})[1].text.strip()
            
            length = video.find('span',attrs={"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}).text.strip()
            
            href = video.find('a',attrs = {'id':"thumbnail","class":"yt-simple-endpoint inline-block style-scope ytd-thumbnail"})["href"]
            
            link = 'https://www.youtube.com'+href
            
            source= requests.get(link).text
            soup_link =BeautifulSoup(source,'lxml')
            like = soup_link.find("button",attrs={"title": "I like this"}).get_text()
    
            dislike = soup_link.find("button",attrs={"title": "I dislike this"}).get_text()
    
            subscriber = soup_link.find("span", attrs={"class": "yt-subscriber-count"}).get_text()
        except AttributeError:
            print('AttributeError ',count)
            err += 1
            continue
        except IndexError:
            print('IndexError ',count)
            err += 1
            continue
        time.sleep(2)
        video_df.iloc[count] = [title,view,channel,uploadtime,length,link,subscriber,like,dislike]
        count += 1
    
    video_df.drop(video_df.tail(err).index,inplace=True) 
    print('csv generated')
    return video_df

# =============================================================================
# auto run for multiple times
# =============================================================================
def job():
    
    
    currentDT = datetime.datetime.now()
    
    currenttime = currentDT.strftime("%m%d%Y_%H%M%S")
    
    filename = "autorun/video_" + currenttime + ".csv"
    #filename = 'video_03102020_0930pm.csv'
    print(filename)
    
    video_df = YT_scrape()
    
    video_df.to_csv(filename)
    print('csv saved')
# =============================================================================
# main, run 20 times of search, with 3 h time interval
# =============================================================================
if __name__=="__main__":
    for i in range(20):
        job()
        waittime = 10800 # here waittime in seconds
        time.sleep(waittime)  


