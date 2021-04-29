from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import traceback

url = 'https://shopee.vn'

def correct_url(url): 
	if not url.startswith("http://") and not url.startswith("https://"):
		url = "http://" + url
	return url

def scrollDown(browser, numberOfScrollDowns):
	body = browser.find_element_by_tag_name("body")
	while numberOfScrollDowns >=0:
		body.send_keys(Keys.PAGE_DOWN)
		numberOfScrollDowns -= 1
		time.sleep(0.3)
	return browser

def crawl_url(url, run_headless=False):
	page_post_url = '?page='
	n_pages = 25
	
	try:
		f = open('./ecommerce_prices/shopee_items_list.txt', 'wb')

		url = correct_url(url)
		browser = webdriver.Chrome()
		browser.get(url)
		time.sleep(1)
		
		content = browser.page_source
		soup = BeautifulSoup(content)
		
		categories = soup.findAll('a', href=True, attrs={'class':'home-category-list__category-grid'})
		
		for category_link in categories:
			category_link = category_link['href']
			f.write((url+category_link+"\n").encode("UTF-8"))
			for page_number in range(n_pages):
				category_url = url + category_link + page_post_url + str(page_number) 
				print (category_url)
				
				
				browser.get(category_url)
				time.sleep(3)
				
				browser = scrollDown(browser, 10)
				category_content = browser.page_source
				category_soup = BeautifulSoup(category_content)
						
				items = category_soup.findAll('div', attrs={'class':"col-xs-2-4 shopee-search-item-result__item"})
														
				for item in items:
					#print (item)
					try:
						link  = item.find('a', href=True)['href']
						print (url+link)
						f.write(("\t"+url+link+"\n").encode("UTF-8"))
						#name  = item.find('div', attrs={'class':"O6wiAW"}).text
						#price = item.find('span', attrs={'class':"_341bF0"}).text
						
						
						#f.write(("\t"+name+"\n").encode("UTF-8"))
						#f.write(("\t"+price+"\n").encode("UTF-8"))
						#print (name, price)
					except:
						traceback.print_exc()
						#break
				#return

		browser.quit()
		f.close()
	except:
		traceback.print_exc()
	
if __name__=='__main__':
	crawl_url(url)
	
	