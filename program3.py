import requests
import bs4

res = requests.get("https://find-my-pg.herokuapp.com")

soup = bs4.BeautifulSoup(res.text,'lxml')

result  = soup.find_all('a',href=True)

# this will prints all the links present on the website.

for link in result:
	if '#' in link['href']:      # this will remove all the # lines from the output
		pass
	else:
		print(link['href'],"\n")