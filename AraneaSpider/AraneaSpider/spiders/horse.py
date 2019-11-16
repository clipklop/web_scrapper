"""
    *
    * Simple app to scrap horses from a webpage using Scrapy.
    *
"""

import scrapy


HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


class HorseSpider(scrapy.Spider):
    name = 'mi'

    def start_requests(self):
        urls = ['https://treehouse-projects.github.io/horse-land/index.html',
        'https://treehouse-projects.github.io/horse-land/mustang.html']

        return [scrapy.Request(url=url, callback=self.parse, headers=HEADERS) for url in urls]

    def parse(self, response):
        url = response.url
        page = url.split('/')[-1]
        filename = 'horse-{}'.format(page)
        print('URL is: {}'.format(url))

        with open(filename, 'wb') as file:
            file.write(response.body)
        print('Saved file {}'.format(filename))
