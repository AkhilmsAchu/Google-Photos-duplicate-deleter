# Importing BeautifulSoup class from the bs4 module 
from bs4 import BeautifulSoup 
import re
# Opening the html file 
HTMLFile = open("html data to delete.html", "r") 

# Reading the file 
index = HTMLFile.read() 

# Creating a BeautifulSoup object and specifying the parser 
soup = BeautifulSoup(index, 'html.parser') 

# Using the select-one method to find the second element from the li tag 
# rows = soup.find_all("div", {"class": "row"})
# rows = soup.find_all('div[id*="line"]')

regex_id = re.compile('.*line.*')
rows = soup.find_all("div", {"id" : regex_id})
print(len(rows))

regex_class = re.compile('.*col s.*')

links_to_delete = []

for i in rows:#[:1]:

	div_tag = i.find_all("div", {"class" : regex_class})

	links = []
	for text in div_tag:
		a_tags = text.find_all('a')
		for a in a_tags:
			links.append(a['href'])

	links_to_delete+=links[1:]

	# if len(div_tag)<2:
	# 	print(i)
	# 	break
	# 	print('yessssss')
	# div_tag = i.find("div", {"class": "col s5"})

	# a_tag = div_tag.find("a")

	# print(a_tag['href'])
# Using the decompose method 
print('links_to_delete',len(set(links_to_delete)))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\AkhilMs\Desktop\gphotos duplicate delete\data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
#options.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3

driver = webdriver.Chrome(options=options)
import time
for i in links_to_delete[1:2]:
	try:
		driver.get(i)

		WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Delete']")))
		
		driver.find_element(By.CSS_SELECTOR, "[aria-label='Delete']").click()

		WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-mdc-dialog-action='EBS5u']")))
		driver.find_element(By.CSS_SELECTOR, "[data-mdc-dialog-action='EBS5u']").click()

	except Exception as e:
		print(e,'ERROR : ',i)


	