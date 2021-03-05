# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Path to chromedriver
get_ipython().system('which chromedriver')

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Article scraping
# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# One is that we're searching for elements with a specific combination of tag (ul and li) and attribute (item_list and slide, respectively). For example, ul.item_list would be found in HTML as <ul class=”item_list”>

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# Notice how we've assigned slide_elem as the variable to look for the <ul /> tag and its descendent (the other tags within the <ul /> element), the <li /> tags? This is our parent element. This means that this element holds all of the other elements within it, and we'll reference it when we want to filter search results even further. The . is used for selecting classes, such as item_list, so the code 'ul.item_list li.slide' pinpoints the <li /> tag with the class of slide and the <ul /> tag with a class of item_list. CSS works from right to left, such as returning the last item on the list instead of the first. Because of this, when using select_one, the first matching element returned will be a <li /> element with a class of slide and all nested elements within it.


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div' , class_='content_title').get_text() 
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# Image scraping ### Featured Images, using splinter
# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# Find and click the full image button
# The brower find an element by its tag
full_image_elem = browser.find_by_tag('button')[1]

# Splinter will click the image to view its full size 
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL ### Using f-string to add url+img_url_rel
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# Instead of scraping each row, or the data in each <td />, we're going to scrape the entire table with Pandas' .read_html() function.
# 
# df = pd.read_html('http://space-facts.com/mars/')[0] With this line, we're creating a new DataFrame from the HTML table. The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list. Then, it turns the table into a DataFrame.
# 
# df.columns=['description', 'value'] Here, we assign columns to the new DataFrame for additional clarity.
# 
# df.set_index('description', inplace=True) By using the .set_index() function, we're turning the Description column into the DataFrame's index. inplace=True means that the updated index will remain in place, without having to reassign the DataFrame to a new variable.


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# Add the DataFrame to a web application
df.to_html()


browser.quit()



