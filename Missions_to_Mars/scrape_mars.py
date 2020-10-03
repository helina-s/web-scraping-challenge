#!/usr/bin/env python
# coding: utf-8

# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import time
import ssl

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
    

def scrape():
    browser = init_browser()
    mars_info= {}

    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)

    time.sleep(1)

    #scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    #Retrieve the latest news title and paragraph
    news_title = soup.find_all('div', class_='content_title')[1].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

#JPL Mars Space Images - Featured Image
#Visit the url for JPL Featured Space Image.
    main_url = 'https://www.jpl.nasa.gov'
    image_url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')
    img_soup.find_all('img')

#Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the 
#url string to a variable called featured_image_url.
    featured_image_url = main_url + (img_soup.find_all('img')[3]['src'])
# print(f'featured_image_url = {featured_image_url}')


#Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, 
#Mass, etc.
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)

    ssl._create_default_https_context = ssl._create_unverified_context
    tables = pd.read_html(mars_facts_url)

    mars_facts_df = tables[0]
    mars_facts_df.columns=['Description', 'Value']
    mars_facts_df

    mars_facts_df.to_html()
#Save as html file
    mars_facts_df.to_html('mars_facts.html')


#Mars Hemispheres
#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres
    base_url = 'https://astrogeology.usgs.gov'
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)
    hem_html = browser.html
    hem_soup = bs(hem_html, 'html.parser')

# Retreive all items that contain mars hemispheres information
    results = hem_soup.find_all('div', class_='item')
    hemisphere_image_urls = []

#Loop through each hemisphere data
    for result in results: 
        title = result.find('h3').text
        img_url = result.find('a', class_='itemLink product-item')['href']
        browser.visit(base_url + img_url)
        img_html = browser.html
        img_soup = bs(img_html, 'html.parser')
        image_url = base_url + img_soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "img_url" : image_url})
        time.sleep(1)


    #Store data in a dictionary
    mars_info = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": open("mars_facts.html").read(),
        "hemisphere_image_urls": hemisphere_image_urls
    }    

    #Close the browser after scraping
    browser.quit ()

    #Return results
    return mars_info

if __name__ == "__main__": 
    pass
