import scrapy

class amzASIN(scrapy.Spider):

    name='asinScrapper'

    start_urls=['https://www.amazon.in/s?k=trimmers']

    def parse(self, response):
        asins=response.css('div[data-asin]')
        for asin in asins:
            item = {'asin':asin.css('::attr(data-asin)').get()}
            yield item
        # god damn this yield stuff

        nextPage=response.css('li.a-last').css('a')
        if nextPage is not None:
            yield response.follow('https://www.amazon.in'+nextPage.attrib['href'],callback=self.parse)
        