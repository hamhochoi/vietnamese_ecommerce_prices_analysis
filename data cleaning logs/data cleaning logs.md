# Data cleaning logs

## Step 1: Convert .txt files into .csv files
	- Each .txt file contain link, name and price of items within different categories.
	- Each .txt file follow a unique structure: first line is link, second line is name, third line is price of a item. Then there is a '-----' in forth line act as a determined symbol.
	- Confirm by ensuring the number of items before and after cleaning are the same.

## Step 2: Remove dupplicates
	- In each spreadsheet, it may have dupplicates. 
	- Use google spreadsheets tools to remove dupplicates 

## Step 3: Convert prices from string to number
	- filter out the prices contain range (ex: 10000d-20000d)
	- use pandas to convert string to number
	

## Step 4: Concatenate all list of items of a platform each day together
	- To make crawling process faster, list of items was paralell crawled into multiple files.
	- This step to combine those files.

## Step 5: Add categories to each item.
	- Use "lazada_list_item.txt" file to generate category of each item on lazada platform. Do the same with others platforms.


## Step 6: Join tables to filter the common items during crawling data between days.
	- Items crawled each day on each website maybe different because items on ecommerce website aren't static, they change day after day.
	- Filter the common items (links, names) to ensure the fair comparision in prices.
	- Filter by joining tables of items day after day.
