from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(response, 'html.parser')
i = 1
for anchor in soup.find_all("a"):
    print(str(i) + ' ' + anchor.get('href', '/'))
    i = i+1