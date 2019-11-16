"""
    * Simple app to scrap horses from a webpage...yeah I know!
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

#print(soup.prettify())

# divs = [div for div in soup.find_all('div', {'class': 'featured'})]

featured_header = soup.find('div', {'class': 'featured'}).h2.get_text()
print(featured_header)

ahrefs = [link.get('href') for link in soup.find_all('a')]
print(ahrefs)
