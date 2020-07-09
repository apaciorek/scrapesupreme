from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from time import sleep
import re
import csv




driver = webdriver.Chrome()

#actions = ActionChains(driver)

driver.get("https://www.supremenewyork.com/shop/new")

new_items = driver.find_elements_by_xpath('//a[@style="height:81px;"]')
item_links = []
for item in new_items:
	item_link = item.get_attribute("href")
	item_links.append(item_link)

# print(item_links)
# print(len(item_links))

csv_file = open('supreme_newdrops_uk.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

for link in item_links:
     item_dict = {}
     driver.get(link)
     sleep(1)
     try: 
     	details = driver.find_element_by_xpath('//div[@id="details"]')
     	item_name = details.find_element_by_tag_name('h1').text
     except: 
     	print(f'Couldn\'t get name!')
     	item_name = "Name Not Found"
     try:
     	#pricing = driver.frind_element_by_xpath('//p[@class="price"]')
     	item_price = details.find_element_by_tag_name('span').text
     except:
     	print(f'Couldn\'t get price!')
     	item_price = "Price Not Found"
     try:
     	item_description = driver.find_element_by_xpath('//p[@class="description "]').text
     except:
     	print(f'Couldn\'t get description')
     	item_description = "Description Not Found"
     try:
     	item_color = driver.find_element_by_xpath('//p[@class="style protect"]').text
     except:
     	print(f'Couldn\'t get item color')
     	item_color = "Color Not Found"
     try:
     	item_availability = driver.find_element_by_xpath('//b[@class="button sold-out"]').text
     except:
     	#print(f'Item In Stock')
     	item_availability = "In Stock"
     try:
          img = driver.find_element_by_xpath('//img[@id="img-main"]')
          item_image = img.get_attribute("src")
     except:
          print(f'No Item Image')
          item_image = "Image Not Found"
     


     item_dict['Name'] = item_name
     item_dict['Color'] = item_color
     item_dict['Description'] = item_description
     item_dict['Price'] = item_price
     item_dict['Availability'] = item_availability
     item_dict['Image'] = item_image

     writer.writerow(item_dict.values())

     # print('ItemName = {}'.format(item_name))
     # print('ItemColor = {}'.format(item_color))
     # print('ItemDescription = {}'.format(item_description))
     # print('ItemPrice = {}'.format(item_price))
     # print('ItemAvailability = {}'.format(item_availability))

csv_file.close()
driver.close()


