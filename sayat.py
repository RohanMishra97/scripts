from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(username,password) :
	driver.get('http://www.facebook.com/login')
	elem = driver.find_element_by_name('email')
	elem.clear()
	elem.send_keys(username)
	elem = driver.find_element_by_name('pass')
	elem.clear()
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)

def sayat(link,message):
	driver2 = webdriver.Chrome()
	driver2.get(link)
	elem = driver2.find_element_by_name('write')
	elem.clear()
	elem.send_keys(message)
	elem = driver2.find_element_by_class_name('btn-primary')
	elem.click()
	time.sleep(3)
	driver2.close()

username = raw_input('Input Email - ')
password = raw_input('Input Password - ')
message = raw_input("What's your message? ")
driver = webdriver.Chrome()
login(username, password)

time.sleep(4)
print driver.title
Links = []
while True:
	elems = driver.find_elements_by_css_selector(".userContent a")
	for elem in elems:
		link = elem.get_attribute('href')
		if(link not in Links):
			if ('sayat.me' in link):
				print link
				Links.append(link)
				time.sleep(2)
				sayat(link,message)
			# else :
			# 	if (len(link) < 50):
			# 		print link
			# 	else :
			# 		print link[0:40] + "..."
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")	

time.sleep(10)
driver.close()
