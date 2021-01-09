# web-scraping-challenge
In this challenge, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. I used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to accomplish this task. 

## Step 1 - Scraping
Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that I can reference later.

### JPL Mars Space Images - Featured Image
Visited the url for JPL Featured Space Image and used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

### Mars Facts
Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. I also used Pandas to convert the data to a HTML table string.

### Mars Hemispheres
Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. I used a Python dictionary to store the data using the keys img_url and title and appended the dictionary with the image url string and the hemisphere title to a list, containing one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application
For this step, I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs in the first step.
