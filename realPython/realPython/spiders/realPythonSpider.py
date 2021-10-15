import scrapy
'''
main todo: how to load infinte scroll using scrapy and parse that
'''
class realPythonSpider(scrapy.Spider):

    name='realPython'

    start_urls=['https://realpython.com/']

    def parse(self, response):
        articles=response.css('img.card-img-top.m-0.p-0.embed-responsive-item.rounded')
        for article in articles:
            item={
                'article header':article.css('::attr(alt)').get(),
                'article image':article.css('::attr(src)').get()
            }
            yield item