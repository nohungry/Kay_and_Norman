import time
import scrapy

from books.items import BooksItem
from scrapy.http import Request

class DrawBooksSpider(scrapy.Spider):
    name = 'draw_books'
    allowed_domains = ['books.com.tw']
    start_urls = ['https://www.books.com.tw/web/books_bmidm_0303/?o=1&v=1&page=1']

    def parse(self, response):
        getItems = response.css('.wrap .item')
        for getItem in getItems:
            item = BooksItem()
            title = getItem.css('h4 a::text').get()
            author = getItem.css('.info a::text').getall()[0]
            price = getItem.css('.price_box .set2 strong::text').getall()[1]
            item['title'] = title
            item['author'] = author
            item['price'] = price
            yield item

        next_page = response.css('.wrap .nxt::attr(href)').get()
        print(next_page)
        
        # 下面這一段老師是教 yield response.follow(next_page,  self.parse)
        # 但是我試了就是沒有過，會是因為爬取不同網頁的關係嗎？ 他爬的是 PTT
        page = 0
        if next_page is not None and page < 3:
            page += 1
            # time.sleep(3)
            yield Request(start_urls=next_page, callback=self.parse)