#!/usr/bin/env python
# coding: utf-8

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')



slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# convert browser html to soup
html = browser.html
Hemi_soup = soup(html, 'html.parser')

# parse Hrefs for sites containing hemishphere info, save hrefs into 'href' list
link_soup= Hemi_soup.find('div',class_='collapsible results')
hrefs = []

for link in link_soup.find_all('a'):
    if link.get('href') not in hrefs:
        hrefs.append(link.get('href'))

# Loop through hrefs list and create f string urls by combining 'https://marshemispheres.com/' with href
# save results in url_list
url_list = []

for h in hrefs:
    url_list.append(f'{url}{h}')

# loop through url_list to acces web pages for each hemishere    
for u in url_list:
# Create hemishpere dict and zero out title and image variable before each pass
    hemispheres = {}
    titles=0
    images=0
    
# visit each url in loop convert browser to html soup (m_soup)
    browser.visit(u)   
    html = browser.html
    m_soup = soup(html, 'html.parser')

# Parse jpg href from each hemisphere url
    step_1 = m_soup.find('div',class_='downloads')
# loop through all href instances and only choose href's with jpg 
    for step in step_1.find_all('a'):
        if 'jpg' in (step.get('href')):
# Save jpg href to images variable
            images=step.get('href')
# assign dictionary values to keys img_url and title
    hemispheres['img_url']=f'{url}{images}'
    hemispheres['title']=m_soup.find('h2').text
# Append list of hemispheres dictionaries
    hemisphere_image_urls.append(hemispheres)
# end browser for next url
    browser.back()
    

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()



