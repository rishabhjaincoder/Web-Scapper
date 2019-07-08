import bs4
import requests

res  = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text,'lxml')

result= soup.select(".mw-headline")

#result= soup.select(".toctext")

for i in result:
	print(i.text,"\n")

# this will print all the headings of that specific URL.