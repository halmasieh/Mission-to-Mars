# Mission-to-Mars
We cover web scraping and various tools needs to extracting information from the active websites. 

We perform the following steps: 
   - Use Chrome Driver tools to identify HTML components.
   - Use BeatifulSoup and Splinter to automate the scrape.
   - Use Mongo to store the data
   - Use Flask to display data

Web scraping is a method of gaining data from different resources quickly and instead of using each website, we manually extract data. 
The web scraping process is automated using a programming scrape. On smaller scale, web scraping automates tedious tasks for personal projects. 
For example, if you're collecting current news on a specific subject, web scraping can make it a simple process. 
Instead of visiting each website and copying an article, a web scraping script will perform those actions and save the scraped data for later analysis.
Web scraping is used by organizations worldwide to extract online data for analysis. Large companies employ web scraping to assess their reputations or track their competitors' online presence.



## Resources
- Data Sources: [Nasa wensite](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
- Software: [Jupyter Notebook](https://www.anaconda.com/products/individual), [Python 3.7.6](https://www.python.org/downloads/) and [Visual Studio Code](https://code.visualstudio.com/) 
- Module: Splinter, Pandas, Flask, webdriver_manager.chrome, PyMongo, BeautifulSoup


## Summary
The project is done as follows:
   - Automate a web browser to visit different websites to extract data about the Mission to Mars.
   - Admire images of Mars’s hemispheres online and realized that the site is scraping-friendly.
   - Scrape full-resolution images of Mars’s hemispheres and the titles of those images using BeautifulSoup and Splinter. 
   - Store the scraped data on a Mongo database.
   - Use a web application to display the data, and alter the design of the web app to accommodate these images.
