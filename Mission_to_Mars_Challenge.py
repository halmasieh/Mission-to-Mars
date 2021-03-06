# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

]:

# Path to chromedriver
get_ipython().system('which chromedriver')


# Set the executable path and initialize the chrome browser in splinter
# executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
# browser = Browser('chrome', **executable_path)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


slide_elem.find("div", class_='content_title')


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
# full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# ### Mars Facts

df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


df.to_html()


# ### Mars Weather


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

results = browser.find_by_css('a.product-item img')
for result in range(len(results)):
    hemisphere = {}
    
    # Identify and return title of listing
    browser.find_by_css('a.product-item img')[result].click()
    sample_img= browser.find_by_text('Sample').first
    hemisphere['img_url'] =sample_img['href']
    hemisphere['title']= browser.find_by_css('h2.title').text
    
    #title = browser.find('h3', class_='itemLink product-item')[result]
    # Identify and return link to listing
    #link = result.a['href']

    # Run only if title and link are available
    #if (title and link):
        # Print results
        #print('-------------')
        #print(title)
        #print(link)

        # Dictionary to be inserted as a MongoDB document
    
    hemisphere_image_urls.append(hemisphere)
    browser.back()
    

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()





