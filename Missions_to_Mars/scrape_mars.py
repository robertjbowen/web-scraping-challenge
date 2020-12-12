# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:34:23 2020

@author: Rob Bowen
"""

import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



def init_browser():
    
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}


    # Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    soup = BeautifulSoup(browser.html, 'html.parser')

    mars_data['news_title'] = soup.find('li', class_='slide').find_all(class_='content_title')[0].text
    mars_data['news_p'] = soup.find('li', class_='slide').find_all(class_='article_teaser_body')[0].text


    # JPL Mars Space Images - Featured Image
    site_url = 'https://www.jpl.nasa.gov'
    search_criteria = 'spaceimages'
    location = 'Mars'
    query_url = f'{site_url}/{search_criteria}/?search=&category={location}'
    browser.visit(query_url)

    soup = BeautifulSoup(browser.html, 'html.parser')

    images = soup.find('article')
    image_url = images.find('a')['data-fancybox-href']
    mars_data['featured_image_url'] = site_url + image_url
    

    # Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    pd.read_html(facts_url)[0].to_html('templates/mars_facts.html')
    mars_facts = pd.read_html(facts_url)[0]
    mars_facts.rename(columns={0:"Description", 1:"Mars"},inplace=True)
    mars_facts = mars_facts.set_index('Description')
    mars_data['mars_facts'] = mars_facts['Mars'].to_dict()
    # mars_data['mars_facts'] = pd.read_html(facts_url)[0].to_dict()


    #Mars Hemispheres
    site_url = 'https://astrogeology.usgs.gov'
    search_criteria = '/search/map/Mars/Viking/'
    locations = ['cerberus_enhanced','schiaparelli_enhanced', 'syrtis_major_enhanced','valles_marineris_enhanced']
    hemisphere_image_urls = []

    for location in locations:
        query_url = f'{site_url}{search_criteria}{location}'
        browser.visit(query_url)
        soup = BeautifulSoup(browser.html, 'html.parser')
        title = soup.find('h2', class_='title').text[:-9]
        image_url = soup.find('img', class_='wide-image')['src']
        img_url = site_url + image_url
        hemisphere_dict = {'title': title, 'img_url': img_url}
        hemisphere_image_urls.append(hemisphere_dict)

    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    
    browser.quit()

    return mars_data
