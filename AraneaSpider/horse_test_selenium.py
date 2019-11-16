#

from bs4 import BeautifulSoup
from selenium import webdriver

import time


driver = webdriver.Chrome(executable_path="/Users/clipklop/Stuff/scripts/chromedriver")
driver.get('https://treehouse-projects.github.io/horse-land/index.html')

time.sleep(5)

page_html = driver.page_source
soup = BeautifulSoup(page_html, 'html.parser')

print(soup.prettify())
