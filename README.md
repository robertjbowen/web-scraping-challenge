# web-scraping-challenge


***

The purpose of this challenge is to use html code to create a web interface to display data and images scraped from websites using python webscraping techniques. The site allows the viewer to run the web scraping function to refresh the News and featured images information on demand. 

***

### Documents in this repository are:

1. Missions_to_Mars directory - Folder containing all of the project code

	* MarsApp.py - Base python file containing Flask apps to generate the webpage and collect data

	* scrape_mars_py - Python file called by MarsApp to search multiple websites to pull specific data and images and packe them into a data dictionary

	* mission_to_mars.ipynb - python notebook generated in Jupyter Lab to develop and test the scrape_mars code

	* Mongo_development.ipynb - python notebook generated in Jupyter Lab to develop and test the MarsApp code

	* templates directory - folder containing the html files

		* index.html - This is the html code to generate the web Landing Page called by the index app in MarsApp.

		* mars_facts.html - html table code generated by the mars_facts section of the scrape_mars code 

2. images directory - contains images of the WebPage outputs and scrape sources for display in the ReadMe

***
### Design concept:


## Initialization:

1) Prior to running the MarsApp you must establish a connection to the Mongo server and open the mongo shell by opening to instances of your computer's command prompt and entering mongod into the first and and mongo into the second. These must remain open in the background. 

2) Within your Python development environment open and run the MarsApp.py file.
  
Note: You must initialize the Mars_db database by visiting 127.0.0.1:5000/scrape in your browser the first time, before the landing page will display any data.


## MarsApp.py:

1) First the MarsApp Python code uses pymongo to initially create or establish a connection to a Mongo database called Mars_db. 

2) Next it uses a flask app to create a route "called index" that imports the MarsData collection from the Mars_db database and and opens an html template file called index.html to render the data on a webpage at 127.0.0.1:5000. 

3) The code has a second route called "scraper" that is called by a button on the webpage or can be run directly by typing 127.0.0.1:5000/scrape. This route calls the scrape_mars.py file and updates the MarsData collection in the Mars_db database.


## scrape_mars.py:

1) This code is called by MarsApp.py when the "scraper" route is activated.

2) This Python code conducts four seperate scraping functions and saves the results of each into a data dictionary called mars_data which it returns to MarsApp.py where it is updated into the MarsData collection in the Mars_db Database.

***

Mars News - Uses Splinter to open a browser connection to 'https://mars.nasa.gov/news/' and then uses BeautifulSoup to parse the sites html into a variable called soup. The text values of the 'content title' and the 'article teaser body' of the first news article slide are scraped and saved to the mars_data dictionary under the keys: 'news_title' and 'news_p'

<p>
    <img src="https://github.com/robertjbowen/web-scraping-challenge/blob/main/images/scrapeNews.png"/>
    <br>
    <em>https://mars.nasa.gov/news/ with inspect highlighting location of scraped material</em>
</p>

***

JPL Mars Space Images - Again uses Splinter and BeautifulSoup to open a browser connection to 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'. This function scrapes the image url from the html image href called 'data-fancybox-href' of the current Featured Image from the page. The site url is concatinated with the scraped image url to create a complete url then saved in the mars_data dictionary under the key 'featured_image_url'.

<p>
    <img src="https://github.com/robertjbowen/web-scraping-challenge/blob/main/images/scrapeFeaturedImg.png"/>
    <br>
    <em>https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars with inspect highlighting location of scraped material</em>
</p>
***

Mars Facts - Uses Pandas pd.read_html function to scrape all of the tables from the website 'https://space-facts.com/mars/'. A DateFrame is created from the first table on the page and is formatted to create column labels and set the 'Description Column as the table index. This DataFrame is written to an html file in the templates folder called mars_facts.html and is saved in the mars_data dictionary under the key 'mars_facts'.

<p>
    <img src="https://github.com/robertjbowen/web-scraping-challenge/blob/main/images/Mars_Facts.png"/>
    <br>
    <em>https://space-facts.com/mars/ - showing location of scraped table</em>
</p>
***

Mars Hemispheres - Uses a list of the four Marsian Hemispheres and the Splinter and BeautifulSoup methodology from above on the web pages 'https://astrogeology.usgs.gov/search/map/Mars/Viking/{list items} to scrape the image titles and urls for the enhnaced images of each hemisphere. The title text is truncated to remove the word ' enhanced' and the image url is concatenated to the site url to create a full image url. The title and image url values are saved to a data dictionary called hemisphere_dict. The dictionary is then appended to a list called hemisphere_image_urls. Once all four images are scraped, the final list is saved to the mars_data dictionary under the key 'hemisphere_image_urls'.

<p>
    <img src="https://github.com/robertjbowen/web-scraping-challenge/blob/main/images/Mars_Hemispheres.png"/>
    <br>
    <em>https://astrogeology.usgs.gov/search/map/Mars/Viking/ showing thumbnails of all four images to be scraped</em>
</p>
***

## index.html

The third major piece to this project is the web image template used to display all of the scraped images and data. The file uses  bootstrap column and row style template formatting to display the information in 5 rows.

Row 1 - Header - is a simple preformatted jumbotron header containing a single button with an href to activeate the scrape function

Row 2 - Mars News - loads and displays the values from the MarsData dictionary for the keys news_title and news_p 

Row 3 - Featured Image and Facts - uses bootstrap to divide the row into two boxes of widths 7 and 5. The first box displays the  image from MarsData.featured_image_url styling the image to fill the entire width of the box. The height is not fixed as the images vary in dimension (the image size ratio is locked so the height adjusts in proportion to the width automatically). The second box displays the mars_facts table. The table structure was built from the mars_data.html file scraped from the site and imported into index.html.

Rows 4 and 5 - Hemisphere Images - loads, styles, and displays the enhanced hemisphere images in two rows of two images each with their titles displayed beneath each image. Like above, width styling locks the image width to the width of the column and additional styling creates a border around each image. 

<p style='margin: auto; width: 50%'>
    <img src="https://github.com/robertjbowen/web-scraping-challenge/blob/main/images/FullPage.png"/>
    <br>
    <em>127.0.0.1:5000 - Full page view of final web site rendering</em>
</p>

***
