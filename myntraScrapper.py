from packages import *

chrome_driver_path = 'C://Drivers//chromedriver.exe'
chrome_service = Service(chrome_driver_path)
chrome_options = Options()
# Open URL
base_url = "https://www.myntra.com/"


def scrapperMyntra(key_word, limit_for_each_keywords,data_myntra_list):

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    path_param = key_word.replace(" ", "-")
    url = base_url + path_param
    driver.get(url)
    time.sleep(5)

    product_element = driver.find_element(By.CLASS_NAME, 'results-base')
    product_list = product_element.find_elements(By.CLASS_NAME, 'product-base')
    for scrappeCnt,product in enumerate(product_list): # one chunk of products
        if scrappeCnt >= limit_for_each_keywords:
            break
        
        data_myntra = {}

        product_id = product.get_attribute('id')

        try:
            rating = product.find_element(By.CLASS_NAME, 'product-ratingsContainer').find_element(By.TAG_NAME,'span').text
            ratingCnt = product.find_element(By.CLASS_NAME, 'product-ratingsContainer').find_elements(By.CLASS_NAME,'product-ratingsCount')[0].text[2:]
        except Exception as e:
            rating = None
            ratingCnt=None
            print(f"Error getting rating: {e}")

        try:
            a_tag = product.find_element(By.TAG_NAME, 'a')
            href = a_tag.get_attribute('href')
            brand = a_tag.find_element(By.CLASS_NAME, 'product-productMetaInfo').find_element(By.CLASS_NAME, 'product-brand').text
            title = a_tag.find_element(By.CLASS_NAME, 'product-productMetaInfo').find_element(By.CLASS_NAME, 'product-product').text
            size = a_tag.find_element(By.CLASS_NAME,'product-sizes').find_element(By.TAG_NAME,'span').get_attribute('innerHTML')
            img_link = a_tag.find_element(By.TAG_NAME,'source').get_attribute('srcset') # as of now only one, it could be list of images link
            try:
                actualPrice = a_tag.find_element(By.CLASS_NAME,'product-strike').text
                discountedPrice = a_tag.find_element(By.CLASS_NAME,'product-discountedPrice').text
                discountPercent = a_tag.find_element(By.CLASS_NAME,'product-discountPercentage').text
            except Exception as e:
                actualPrice = a_tag.find_element(By.CLASS_NAME,'product-price').text
                discountedPrice = actualPrice
                discountPercent = 0
                print(f"No Discounted Prize: {e}")
        except Exception as e:
            print(f"Error: {e}")

        

        data_myntra['product_id'] = product_id
        data_myntra['keywords_search'] = key_word
        data_myntra['description'] = {}
        data_myntra['description']['Product_link'] = href
        data_myntra['description']['brand'] = brand
        data_myntra['description']['title'] = title
        data_myntra['description']['img_link'] = img_link
        data_myntra['description']['actualPrice'] = actualPrice
        data_myntra['description']['discountedPrice'] = discountedPrice
        data_myntra['description']['discountPercent'] = discountPercent
        data_myntra['description']['size'] = size
        data_myntra['description']['rating'] = rating
        data_myntra['description']['rating_cnt'] = ratingCnt

        data_myntra_list.append(data_myntra)
        print(f"scrapped for keyword: {key_word}, scrape count: {scrappeCnt + 1}")
        
    driver.quit()
        
