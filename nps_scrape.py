## National Park - Web Scrape
# Data retrieved from National Park Service
# https://www.nps.gov/state/ma/index.htm
###########################################

import requests as re
from bs4 import BeautifulSoup as bs

if __name__ == '__main__':
	# abbreviated list of States
	states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
	"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
	"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
	"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
	"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

	print("#### National Park Service - Web Scaper ####")
	print("############################################")
	print("Available States: ")
	for i in range(0,len(states),5):
		print(states[i:i+5])
	print("############################################")
	print("Enter State: " )
	state = (input().upper())
	while True:
		if state not in states:
			print("Error: Not valid State")
			print("Enter State: ")
			state = (input().upper())
		else:
			break

	# grab State's park page
	url = "https://www.nps.gov/state/%s/index.htm" % state
	result = re.get(url)
	page = result.content
	soup = bs(page,"lxml")
	
	# find parks
	parks = soup.find_all("li","clearfix")
	# within each park:
	for park in parks[:-1]:
		park_name = park.find('h3').text
		park_type = park.find('h2').text
		park_loc = park.find('h4').text
		parK_desc = park.find('p').text

		print("State: %s" % state)
		print("Park Name: %s" % park_name)
		print("Park Type: %s" % park_type)
		print("Park Name: %s" % park_loc)
		print("Park Desc: %s" % parK_desc)
