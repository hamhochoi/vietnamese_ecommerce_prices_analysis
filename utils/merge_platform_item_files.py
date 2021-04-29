import os
import pandas as pd

folder = 'converted-prices-to-numberic/2020-12-28'
files = os.listdir(folder)

out_path = 'merge_total_items_each_platform'
out_path = os.path.join(out_path, folder.split('/')[-1])

if (not os.path.exists(out_path)):
	os.mkdir(out_path)

df_lazada = pd.DataFrame({"links":[], "names":[], "prices":[]})
df_shopee = pd.DataFrame({"links":[], "names":[], "prices":[]})
df_sendo  = pd.DataFrame({"links":[], "names":[], "prices":[]})
df_tiki   = pd.DataFrame({"links":[], "names":[], "prices":[]})

for file in files:
	print (file)
	if ('lazada_items_details' in file):
		file_path = os.path.join(folder, file)
		df_tmp = pd.read_excel(file_path, decoding='utf-8-sig')
		df_lazada = pd.concat([df_lazada, df_tmp])
	elif ('sendo_items_details' in file):
		file_path = os.path.join(folder, file)
		df_tmp = pd.read_excel(file_path, decoding='utf-8-sig')
		df_sendo = pd.concat([df_sendo, df_tmp])
	elif ('shopee_items_details' in file):
		file_path = os.path.join(folder, file)
		df_tmp = pd.read_excel(file_path, decoding='utf-8-sig')
		df_shopee = pd.concat([df_shopee, df_tmp])
	elif ('tiki_items_details' in file):
		file_path = os.path.join(folder, file)
		df_tmp = pd.read_excel(file_path, decoding='utf-8-sig')
		df_tiki = pd.concat([df_tiki, df_tmp])
		

print (df_lazada.shape[0])
print (df_sendo.shape[0])
print (df_shopee.shape[0])
print (df_tiki.shape[0])

if (df_lazada.shape[0] > 0):
	df_lazada.to_excel(os.path.join(out_path, "lazada_total_items_detail.xlsx"), index=False, encoding='utf-8-sig')
if (df_sendo.shape[0] > 0):
	df_sendo.to_excel(os.path.join(out_path, "sendo_total_items_detail.xlsx"), index=False, encoding='utf-8-sig')
if (df_shopee.shape[0] > 0):
	df_shopee.to_excel(os.path.join(out_path, "shopee_total_items_detail.xlsx"), index=False, encoding='utf-8-sig')
if (df_tiki.shape[0] > 0):
	df_tiki.to_excel(os.path.join(out_path, "tiki_total_items_detail.xlsx"), index=False, encoding='utf-8-sig')