"""
    *
    * Simple app to scrap horses from a webpage using Scrapy.
    *
"""

import scrapy


class HorseSpider(scrapy.Spider):
    name = ''

    def start_requests(self):
        urls = ['https://treehouse-projects.github.io/horse-land/index.html',
        'https://treehouse-projects.github.io/horse-land/mustang.html']

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        # return super().parse(response)
        pass
