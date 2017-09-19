#!/usr/bin/env python3
#pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib

file = open('Document.htm', 'r')
htmlDoc = file.read()
file.close()
soup = BeautifulSoup(htmlDoc, 'html.parser')

tables = soup.find_all('table')
for table in tables:
	for row in table.find_all('tr'):
		for cell in row.find_all('td'):
			print(cell.string)
