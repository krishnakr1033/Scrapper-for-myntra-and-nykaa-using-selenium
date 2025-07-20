from nykaaScrapper import *
import json

data_nykaa = []
# keys:
    # - product_id - ok
    # - keywords_search - ok
    # - Description:
        #   - link - ok
        #   - img_url = []- ok
        #   - originalPrize - ok
        #   - Prize - ok
        #   - Discount - ok
        #   - size -ok"
        #   - Rating - ok
        #   - brand - ok
        #   - title - ok

key_words = ["white shirt","black suit","denim jeans", "summer kurti", "co-ord set", "oversized t-shirt", "sneakers", "blue linen pants", "pink blazer for women","yellow maxi dress"]
# black dress changed to black suit as it takes the search to different DNS, it goes to diff base url automatically(nykaafashion.com instead of nykaa.com)

# path_params = []
# for words in key_words:
#     path_params.append(words.replace(" ","%20"))


limit_for_each_keywords = 10
for key_word in key_words:
    scrapperNykaa(key_word,limit_for_each_keywords,data_nykaa)
    time.sleep(1)


# Save the data to a JSON file
with open('data_nykaa.json', 'w') as f:
    json.dump(data_nykaa, f, indent=4)