from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import traceback
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options
import os
from datetime import date


url = 'https://shopee.vn'


def crawl(urls, part_number):
	today = date.today()
	today = str(today)

	try:
		os.mkdir('./ecommerce_prices/'+today)
	except:
		pass
		
	fw = open('./ecommerce_prices/{}/shopee_items_details_{}.txt'.format(today, part_number), 'wb')
	fe = open('./ecommerce_prices/{}/shopee_items_error_{}.txt'.format(today, part_number), 'wb')

	for url in urls:
		try:
			url = url.decode('utf-8')
			if ('\t' not in url):
				continue
			
			url = url.split('\t')[-1]
			print (url)
			chrome_options = Options()
			chrome_options.add_argument("--headless")	
			browser = webdriver.Chrome(chrome_options=chrome_options)
			browser.get(url)
			#time.sleep(1)
			
			content = browser.page_source
			soup = BeautifulSoup(content)
			
			item  = soup.find('div',  attrs={'class':'qaNIZv'})
			name     = item.find('span').text
			price      = soup.find('div', attrs={'class':'_3n5NQx'}).text
			
			#print (price)
			#print (name)
			
			
			fw.write((url).encode("UTF-8"))
			fw.write((name+"\n").encode("UTF-8"))
			fw.write((str(price)+"\n").encode("UTF-8"))
			fw.write(('-'*30+'\n').encode("UTF-8"))
			
			browser.quit()
		except:
			traceback.print_exc()
			fe.write((url).encode("UTF-8"))
			#break
	
	fw.close()

def crawl_url(url, run_headless=False):
	page_post_url = '?page='
	n_pages = 25
	n_parts = 8
	
	try:
		fr = open('./ecommerce_prices/shopee_items_list.txt', 'rb')
		urls = fr.readlines()
		leng_part = int(len(urls) / n_parts)
		processes = []
		
		for part_number in range(n_parts):
			try:
				sub_urls = urls[part_number*leng_part:(part_number+1)*leng_part]
				
				#crawl(sub_urls, part_number)
				p = Process(target=crawl, args=(sub_urls, part_number, ))
				p.start()
				processes.append(p)
			except:
				traceback.print_exc()
				#break
				
		for p in processes:
			p.join()
			
	except:
		traceback.print_exc()
		
	
if __name__=='__main__':
	crawl_url(url)
	
	