import os
import pandas as pd


folder = '2020-12-28'
files = os.listdir(folder)

for file in files:
	if ("details" in file and ".txt" in file):
		file_txt = os.path.join(folder, file)
		file_csv = os.path.join(folder, file.split('.txt')[0] + ".csv")
		print (file_txt)
		print (file_csv)
		
		f = open(file_txt, 'rb')
		lines = f.readlines()
		
		df = pd.read_csv(file_csv, encoding='latin1')
		print ("df len:", df.shape[0])
		print ("txt len/4:", len(lines)/4.0)
		
		if (len(lines)/4.0 != df.shape[0]):
			print ("false")
			break