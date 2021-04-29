from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import traceback

url = 'https://tiki.vn'

def correct_url(url): 
	if not url.startswith("http://") and not url.startswith("https://"):
		url = "http://" + url
	return url

def scrollDown(browser, numberOfScrollDowns):
	body = browser.find_element_by_tag_name("body")
	while numberOfScrollDowns >=0:
		body.send_keys(Keys.PAGE_DOWN)
		numberOfScrollDowns -= 1
		time.sleep(0.1)
	return browser

def crawl_url(url, run_headless=False):
	page_post_url = '&page='
	n_pages = 25
	
	try:
		f = open('./ecommerce_prices/tiki_items_list.txt', 'wb')

		url = correct_url(url)
		browser = webdriver.Chrome()
		browser.get(url)
		time.sleep(1)
		
		content = browser.page_source
		soup = BeautifulSoup(content)
		
		target     = soup.find('div', attrs={'class':'Categories__Wrapper-vncu9l-0 knINlg'})
		categories = target.findAll('div', attrs={'class':'blocks'})[0]
		
		#'''
		for category in categories:
			category_link = category['href']
			f.write((category_link+"\n").encode("UTF-8"))
			for page_number in range(1, n_pages):
				category_url = category_link + page_post_url + str(page_number) 
				print (category_url)
				browser.get(category_url)
				time.sleep(3)
				
				browser = scrollDown(browser, 10)
				category_content = browser.page_source
				category_soup = BeautifulSoup(category_content)
						
				item_links = category_soup.findAll('a', href=True, attrs={'class':"product-item"})
				
				for link in item_links:
					link = url + link['href']
					print (link)
					try:
						f.write(("\t"+link+"\n").encode("UTF-8"))
					except:
						traceback.print_exc()
						break
				#return
		#'''
		browser.quit()
		f.close()
	except:
		traceback.print_exc()
	
if __name__=='__main__':
	crawl_url(url)
	
	