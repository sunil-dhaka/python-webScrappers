from typing import ItemsView
import scrapy


class DronesSpider(scrapy.Spider):
    name = 'drones'
    allowed_domains = ['jessops.com/drones']
    start_urls = ['http://jessops.com/drones/']

    def parse(self, response):
        drones=response.css('div.f-grid.prod-row')

        for drone in drones:
            featuresList=[]
            features=drone.css('ul.f-list.j-list').css('li')
            for feature in features:
                featuresList.append(feature.css('li::text').get())
            item={
                'image':drone.css('img.f-width-1-1::attr(src)').get(),
                'title':drone.css('h4').css('a::text').get(),
                'features':featuresList,
                'price':drone.css('p.price.larger::text').get().replace(',',''),
                'inStock':drone.css('ul.f-list.j-list-boolean').css('li::text').get()
            }
            yield item
        pass
