#

from scrapy.http import FormRequest
from scrapy.spiders import Spider


class FormSpider(Spider):
    name = 'formlogin'
    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response):
        formdata = {
            'firstname': 'Mi',
            'lastname': 'Kiss',
            'jobtitle': 'CoolestPrger'
        }
        return FormRequest.from_response(
            response, formnumber=0,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        print('***')
        print(response)
        print('***')
