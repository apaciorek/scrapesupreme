from selenium import webdriver
import selenium.webdriver.support.ui as ui
import re
import csv




driver = webdriver.Chrome()


## Fetching the new drops website

driver.get("https://www.supremenewyork.com/shop/new")



## Creating dictionary of urls for new items

new_items = driver.find_elements_by_xpath('//a[@style="height:81px;"]')
item_links = []
for item in new_items:
	item_link = item.get_attribute("href")
	item_links.append(item_link)




## Creating new csv file 

csv_file = open('supreme_newdrops_week14.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

timevisit = driver.find_element_by_xpath('//time[@data-timezone-offset="-14400"]')
scrape_datetime = timevisit.find_element_by_tag_name('b').text



## Writing header for csv file

writer.writerow(["Name", "Color", "Description", "Price", "Availability", "Image"])




## Cycling through links for every new item; creating dictionary of desired information; writing that dictionary to the csv file

for link in item_links:
     item_dict = {}
     driver.get(link)
     try: 
     	details = driver.find_element_by_xpath('//div[@id="details"]')
     	item_name = details.find_element_by_tag_name('h2').text
     except: 
     	print(f'Couldn\'t get name!')
     	item_name = "Name Not Found"
     try:
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

    



## Writing the date and time of the scrape to the last row of the csv

writer.writerow([scrape_datetime, " ", " ", " ", " ", " "])


## closing the file and exiting the driver

csv_file.close()
driver.close()


