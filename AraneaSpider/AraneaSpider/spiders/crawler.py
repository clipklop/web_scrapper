"""
    * A horse crawler!
"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HorseSpide(CrawlSpider):
    name = 'pony'

    allowed_domains = ['treehouse-projects.github.io']
    start_urls = ['https://treehouse-projects.github.io/horse-land']

    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_horse', follow=True)]

    def parse_horse(self, response):
        url = response.url
        title = response.css('title::text').extract()

        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))
