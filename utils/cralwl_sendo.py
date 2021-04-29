from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import traceback
from selenium.webdriver.chrome.options import Options


url = 'https://www.sendo.vn'

def correct_url(url): 
	if not url.startswith("http://") and not url.startswith("https://"):
		url = "http://" + url
	return url

def scrollDown(browser, numberOfScrollDowns):
	body = browser.find_element_by_tag_name("body")
	while numberOfScrollDowns >=0:
		body.send_keys(Keys.PAGE_DOWN)
		numberOfScrollDowns -= 1
		time.sleep(0.5)
	return browser

def crawl_url(url, run_headless=False):
	page_post_url = '?page='
	n_pages = 25
	
	try:
		f = open('./ecommerce_prices/sendo_items_list.txt', 'wb')

		url = correct_url(url)
		chrome_options = Options()
		chrome_options.add_argument("--headless")	
		browser = webdriver.Chrome(chrome_options=chrome_options)
		#browser = webdriver.Chrome()
		browser.get(url)
		time.sleep(3)
		
		content = browser.page_source
		soup = BeautifulSoup(content)
		
		categories = soup.findAll('li', attrs={'class':'cateMain_2WI2'})
		
		#'''
		for category in categories:
			category = category.find('a', href=True)
			category_link = url + category['href']
			if (category_link == 'https://www.sendo.vn/phu-kien-cong-nghe' or
				category_link == 'https://www.sendo.vn/thoi-trang-nu'):
				print (category_link + " is downloaded! Move to next category_link")
				continue
				
			#print (category_link)
			f.write((category_link+"\n").encode("UTF-8"))
			for page_number in range(1, n_pages):
				category_url = category_link + page_post_url + str(page_number) 
				print (category_url)
				browser.get(category_url)
				time.sleep(3)
				
				browser = scrollDown(browser, 10)
				category_content = browser.page_source
				category_soup = BeautifulSoup(category_content)
						
				links = category_soup.findAll('a', href=True, attrs={'class':"item_3x07"})
				
				for link in links:
					link = url + link['href']
					print (link)
					try:
						f.write(("\t"+link+"\n").encode("UTF-8"))
					except:
						traceback.print_exc()
						#break
				#return
		#'''
		browser.quit()
		f.close()
	except:
		traceback.print_exc()
	
if __name__=='__main__':
	crawl_url(url)
	
	