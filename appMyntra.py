from myntraScrapper import *
import json

data_myntra = []
# keys:
    # - product_id - ok
    # - keywords_search - ok
    # - Description:
        #   - link - ok
        #   - img_url = []- ok
        #   - originalPrize - ok
        #   - Prize - ok
        #   - Discount - ok
        #   - size -ok
        #   - Rating - ok
        #   - brand - ok
        #   - title - ok

key_words = ["white shirt","black dress","denim jeans", "summer kurti", "co-ord set", "oversized t-shirt", "sneakers", "blue linen pants", "pink blazer for women","yellow maxi dress"]

# path_params = []
# for words in key_words:
#     path_params.append(words.replace(" ","-"))


limit_for_each_keywords = 10
for key_word in key_words:
    data_dict = {}
    scrapperMyntra(key_word,limit_for_each_keywords,data_myntra)
    time.sleep(1)


# Save the data to a JSON file
with open('data_myntra.json', 'w') as f:
    json.dump(data_myntra, f, indent=4)
