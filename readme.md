# Scrapper using Selenium

This is having Scrapper for Myntra and Nykaa which could scrap data with multiple informations using **selenium webDriver**. This avoided the bot recognizer and Js dynamically coded information. This could not be done using bs4 as **requests(url)** only takes raw HTML, if any information is dynamic and written in JS this could not be fetched from bs4. Also this gives hints to bot recognizer to halt the scrapping. But the webdriver using selenium opens up the browser, it scrawl over the browser, interacts with the browser which provides realistic appearance to anti-bot system. 

## 🔍 Data Format : JSON

Extracted Data is in file `data_myntra.json` and `data_nykaa.json`. Open it, if anyone wants to check.
```bash
# more or less, this is the structure of the data scrapped
{
 product_id:
 keywords:
 description:{
        link  
        img_url  
        actualPrize 
        discountedPrize  
        discountPercent  
        size  
        rating 
        ratingCnt
        reviewCnt 
        brand  
        title  
    }
}
```


## How to Run

### 1. Install Dependencies
Ensure you have Python installed. Create a virtual environment and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. DownLoad the selenium webdriver corresponding to current version of chrome

```bash
# Cut and Paste the driver .exe file to Drivers folder from dowloaded zip folder
set:  chrome_driver_path = 'C://Drivers//chromedriver.exe'
```

### 3. Test Keywords: 

```bash
# for Myntra
key_words = ["white shirt","black dress","denim jeans", "summer kurti", "co-ord set", "oversized t-shirt", "sneakers", "blue linen pants", "pink blazer for women","yellow maxi dress"]
# for Nykaa
key_words = ["white shirt","black suit","denim jeans", "summer kurti", "co-ord set", "oversized t-shirt", "sneakers", "blue linen pants", "pink blazer for women","yellow maxi dress"]
# black dress changed to black suit as it takes the search to different DNS, it goes to diff base url automatically(nykaafashion.com instead of nykaa.com)
```

### 3. Scrapper App for Myntra and Nykaa
Run the following module to scrape the data:

```bash
# to run (these files have test keywords, handles the data storage, and a fn which call their corresponding scrapper, it will save the data in json format after the process ends)
- appMyntra.py
- appNykaa.py
# Corresponding scrapper (contains fn which implements the scrapping)
- myntraScrapper.py
- nykaaScrapper.py
```

## 🛠️ Implementation Approach

### Implementation of Myntra Scrapper

The script uses Selenium WebDriver with Google Chrome to scrape product data from Myntra based on user-provided keywords.

1. **Driver Setup**: A Chrome WebDriver is initialized with the specified executable path and options.

2. **Keyword-Based Navigation**: The input keyword is formatted to match Myntra's URL pattern and the corresponding search results page is opened in the browser.

3. **Page Loading**: A short delay is added to ensure that dynamic content on the page is fully loaded.

4. **Product Listing Extraction**: The script locates the section containing product listings and iterates through each product until the defined scraping limit is reached.

5. **Data Extraction**:
   - For each product, it extracts details such as:
     - Product ID
     - Product brand and title
     - Sizes available
     - Image link
     - Pricing details (actual, discounted, and discount percentage)
     - Ratings and rating count
     - Product page URL
   - Conditional handling is used for products without ratings or discounts.

6. **Data Structuring**: The extracted information is organized into a dictionary format with clearly labeled fields under a `description` key.

7. **Aggregation**: Each product's data is appended to a master list for further processing or storage.

8. **Cleanup**: Once all relevant products are processed, the browser session is closed to free resources.

---

### Implementation for Nykaa Scrapper

The script uses Selenium WebDriver with Google Chrome to scrape product data from Nykaa's search results based on specified keywords.

1. **Driver Setup**: Initializes the Chrome WebDriver using a predefined executable path and options.

2. **URL Construction**: Converts the input keyword into a URL-encoded string and constructs a full search URL using Nykaa's search format.

3. **Search Page Scraping**:
   - Loads the search result page and waits for the content to load.
   - Identifies the container holding the list of products and iterates over each product up to the specified limit.

4. **Product Link and ID Extraction**:
   - Extracts the product page URL from each product listing.
   - Uses `urlparse` and `parse_qs` to extract the `productId` query parameter from the product URL.

5. **Detailed Product Page Scraping**:
   - Opens each individual product page in a separate browser instance.
   - Waits for the page to load and scrapes:
     - Brand and title
     - Product size
     - Image links (multiple images collected from carousel or gallery)
     - Price information including actual price, discounted price, and discount percentage
     - Ratings, rating count, and number of reviews (if available)

6. **Data Structuring**:
   - Compiles all extracted information into a dictionary structure under a `description` key.
   - Includes metadata like the searched keyword and product ID.

7. **Aggregation**:
   - Appends each product's structured data to a shared list for further use.

8. **Resource Management**:
   - Closes both the **main** and **auxiliary** browser instances after use to free system resources.
