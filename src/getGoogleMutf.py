from sys import argv
import requests
from bs4 import BeautifulSoup
from boto.mturk import price
import re

def makeGoogFinCall(url):
	page = requests.get(url)
	content = page.content
	soup = BeautifulSoup(content, 'html.parser')
	pricesTable = soup.find_all('table', class_='gf-table historical_price')
	mostRecent = pricesTable[0].findAll('td')[0]
	mostRecentPrice = str(mostRecent).split("\n")[1]
	
	pattern = "(\d*\.\d*)"
	match = re.search(pattern, mostRecentPrice)
	return match.group()
	
if __name__ == "__main__":
	url = argv[1]
	print makeGoogFinCall(url)
