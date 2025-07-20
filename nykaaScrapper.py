from packages import *

chrome_driver_path = 'C://Drivers//chromedriver.exe'
chrome_service = Service(chrome_driver_path)
chrome_options = Options()
# Open URL
base_url = "https://www.nykaa.com/search/result/?q="
end_url = "&root=search&searchType=Manual&sourcepage=Search+Page"


def findProductId(product_link):
    # Step 1: Parse the URL
    parsed_url = urlparse(product_link)

    # Step 2: Parse the query parameters into a dictionary
    query_params = parse_qs(parsed_url.query)

    productId = query_params.get('productId', [None])[0]
    return productId



def scrapperNykaa(key_word, limit_for_each_keywords, data_nykaa_list):

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    path_param = key_word.replace(" ", "%20")
    url = base_url + path_param + end_url
    # url = "https://www.nykaa.com/search/result/?q=white%20shirt"+end_url
    driver.get(url)
    time.sleep(5)

    product_element = driver.find_element(By.ID, 'product-list-wrap')
    product_list = product_element.find_elements(By.CLASS_NAME, 'productWrapper')
    for scrappeCnt,product in enumerate(product_list): # one chunk of products
        if scrappeCnt >= limit_for_each_keywords:
            break
        data_nykaa = {}

        try:
            a_tag = product.find_element(By.TAG_NAME, 'a')  
            href = a_tag.get_attribute('href')
            product_id = findProductId(href)
            
            aux_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            aux_driver.get(href)
            time.sleep(5)

            product_description = aux_driver.find_element(By.CLASS_NAME, 'css-14y2xde')

            img_link = []
            # Extracting image links from the product description
            _ = product_description.find_element(By.CLASS_NAME,'css-irizhh').find_elements(By.TAG_NAME, 'img')
            for img in _:
                img_link.append(img.get_attribute('src'))
            
            brand = product_description.find_element(By.CLASS_NAME, 'css-1vqvcw7').find_element(By.CLASS_NAME, 'css-1ttqghx').find_elements(By.TAG_NAME, 'span')[1].text

            details = product_description.find_element(By.CLASS_NAME, 'css-1d5wdox') # right side deails
            title = details.find_element(By.TAG_NAME, 'h1').text
            size = details.find_element(By.TAG_NAME, 'h1').find_element(By.TAG_NAME, 'span').text

            price = details.find_element(By.CLASS_NAME, 'css-1d0jf8e').find_elements(By.TAG_NAME, 'span') # brand
            price_length = len(price)
            actualPrice = price[1].text
            discountedPrice = actualPrice
            discountPercent = '0'
            if price_length>2: discountedPrice = price[2].text
            if price_length>2: discountPercent = price[3].text

            try:
                rating = details.find_element(By.CLASS_NAME, 'css-u2f8dr').find_element(By.CLASS_NAME,'css-m6n3ou').text
                ratingCnt = details.find_element(By.CLASS_NAME, 'css-u2f8dr').find_elements(By.CLASS_NAME,'css-1hvvm95')[0].text
                reviewCnt = details.find_element(By.CLASS_NAME, 'css-u2f8dr').find_elements(By.CLASS_NAME,'css-1hvvm95')[2].text
            except Exception as e:
                print(f"Rating not available: {e}")
                rating = 'N/A'
                ratingCnt = '0'
                reviewCnt = '0'

            aux_driver.quit()
                        
        except Exception as e:
            print(f"Error: {e}")

        

        data_nykaa['product_id'] = product_id
        data_nykaa['keywords_search'] = key_word
        data_nykaa['description'] = {}
        data_nykaa['description']['Product_link'] = href
        data_nykaa['description']['brand'] = brand
        data_nykaa['description']['title'] = title
        data_nykaa['description']['img_link'] = img_link
        data_nykaa['description']['actualPrice'] = actualPrice
        data_nykaa['description']['discountedPrice'] = discountedPrice
        data_nykaa['description']['discountPercent'] = discountPercent
        data_nykaa['description']['size'] = size
        data_nykaa['description']['rating'] = rating
        data_nykaa['description']['rating_cnt'] = ratingCnt
        data_nykaa['description']['review_cnt'] = reviewCnt

        data_nykaa_list.append(data_nykaa)
        print(f"scrapped for keyword: {key_word}, scrape count: {scrappeCnt + 1}")
        
    driver.quit()

