import requests
import bs4

res = requests.get("https://find-my-pg.herokuapp.com")

#print(type(res))                                  # just to verify object type

#print(res.text)                                # this will print just the textual portion of the code

# but this gives us all the html from the website, so here we use beautiful soup to extract the data that we want.

soup = bs4.BeautifulSoup(res.text,'lxml')

#print(type(soup))                                    # just to verify object type

data = soup.select('title')

print(data[0].getText())           # getText() shows only text not the tags