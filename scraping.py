# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
def scrape_all():
    
    # Initiate headless driver for deployment
    #browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "Hemisphere_image_title": hem_scrap(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hem_scrap(browser):
        # 1. Use browser to visit the URL 
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # Create a list to hold the images and titles
        hemisphere_image_urls = []

        # Parse the html with soup
        html = browser.html
        search_soup = soup(html, 'html.parser')

        # Add try/except for error handling
        try:
            # Find the number of results
            results = search_soup.select("div.item")
            
            
            for result in range(len(results)):

                # Create an empty dict to hold the search results
                hemisphere = {}
            
                # Find the link 
                img_url_1 = search_soup.select("div.description a")[result].get('href')
                browser.visit(f'https://astrogeology.usgs.gov{img_url_1}')

                # Parse the new html page with soup
                html = browser.html
                result_soup = soup(html, 'html.parser')
            
                # Scape the full 
                img_url = result_soup.select_one("div.downloads ul li a").get('href')

                # Scrape the title
                title = result_soup.select_one("he.title").get_text()

                # Add the scraped data to the dictionary
                hemisphere = {
                   'img_url': img_url,
                     'title': title
                }  
                # Update the list with the dictionary
                hemisphere_image_urls.append(results)
            
                # Return to the main page
                browser.back() 
        except AttributeError:
            return None    

        # Return the list that holds the dic of img_url and title 
        return hemisphere_image_urls
       
if __name__ == "__main__":
        # If running as script, print scraped data
        print(scrape_all())
    


