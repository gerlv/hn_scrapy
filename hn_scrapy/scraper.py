import scrapy
from scrapy.crawler import CrawlerProcess


class HNLink(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    votes = scrapy.Field()


class HNScrapy(scrapy.Spider):
    name = 'hn_scrapy'
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        for entry in response.css('table.itemlist .athing'):
            id = int(entry.root.attrib.get('id', None))
            votes = response.css('table.itemlist tr span#score_{id}::text'.format(id=id)).extract_first()
            if votes:
                votes = int(votes.split()[0])
            yield HNLink({
                'id': id,
                'url': entry.css('a.storylink::attr(href)').extract_first(),
                'title': entry.css('a.storylink::text').extract_first(),
                'votes': votes,
            })


def run_scraper():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(HNScrapy)
    process.start()


if __name__ == '__main__':
    run_scraper()
