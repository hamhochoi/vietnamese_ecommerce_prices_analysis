import os
import pandas as pd


folder = 'original-data/2020-12-11'
files = os.listdir(folder)
files = files

f_err = open('utils/error.txt', 'w')

for file_num in range(len(files)):
	file = files[file_num]
	if ("details" in file and ".txt" in file):
		file = os.path.join(folder, file)
		print (file)
		f = open(file, 'rb')
		lines = f.readlines()

		links = []
		names = []
		prices = []

		for line_num in range(len(lines)):
			if (line_num+1)%4 == 1:
				link = lines[line_num].decode("utf-8").strip()
				if (link == "------------------------------"):
					f_err.write(file)
					break
				print (file_num, link)
				links.append(link)
			elif (line_num+1)%4 == 2:
				name = lines[line_num].decode("utf-8").strip()
				if (name == "------------------------------"):
					f_err.write(file)
					break
				names.append(name)
				print (file_num, name)
			elif (line_num+1)%4 == 3:
				price = lines[line_num].decode("utf-8").strip()
				if (price == "------------------------------"):
					f_err.write(file)
					break
				print (file_num, price)
				prices.append(price)
				
				
		df = pd.DataFrame({"links":links, "names":names, "prices":prices})
		df.to_csv(file.split(".txt")[0]+".csv", index=False, encoding='utf-8-sig')