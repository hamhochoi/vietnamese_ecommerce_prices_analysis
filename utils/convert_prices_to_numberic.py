import os
import pandas as pd


folder = 'converted-xlsx_removed_dupplicate/2020-12-19'
files = os.listdir(folder)

out_path = 'converted-prices-to-numberic'
out_path = os.path.join(out_path, folder.split("/")[-1])

for file in files:
	file_path = os.path.join(folder, file)
	print (file_path)
	df = pd.read_excel(file_path, decoding='utf-8-sig')
	
	
	########
	# Filter out items contain price ranges (ex: 10000d-20000d)
	len_before_filter = df.shape[0]
	df = df[df["prices"].str.contains('-') == False]
	len_after_filter = df.shape[0]
	
	#######
	# Convert prices from string to numberic
	#'''
	try:
		df[['prices', 'currency']] = df['prices'].str.split(expand=True,)
		df = df.drop(['currency'], axis=1)
	except:
		if ("sendo" in file):
			df[['prices', 'currency']] = df['prices'].str.split('đ', expand=True,)
			df = df.drop(['currency'], axis=1)

		else:
			df[['currency', 'prices']] = df['prices'].str.split('₫', expand=True,)
			df = df.drop(['currency'], axis=1)
		
	try:
		df[['million', 'thounsand', 'dong']] = df['prices'].str.split(".", expand=True,)
		df['dong'] = df['dong'].astype(str)
		idx = df['dong'] == "None"
		df['dong'][idx] = ""
		df['prices'] = df['million'].astype(str) + df['thounsand'].astype(str) + df['dong']
		df  = df.drop(['million', 'thounsand',  'dong'], axis=1)
	except Exception as e:
		df[['thounsand', 'dong']] = df['prices'].str.split(".", expand=True,)
		df['prices'] = df['thounsand'].astype(str) + df['dong']
		df  = df.drop(['thounsand', 'dong'], axis=1)

	if (not os.path.exists(out_path)):
		os.mkdir(out_path)
		
	df.to_excel(os.path.join(out_path, file)	, index=False, encoding='utf-8-sig')
	#'''