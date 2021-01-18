# # This package will contain the spiders of your Scrapy project
# #
# # Please refer to the documentation for information on how to create and manage
# # your spiders.
# import scrapy
# from spiderMan.items import SpidermanItem  # 引入item


# class myspiderSpider(scrapy.Spider):
#     name = "myspider"
#     allowed_domains = ["lab.scrapyd.cn"]
#     start_urls = ['http://lab.scrapyd.cn/']

#     def parse(self, response):
#         mingyan = response.css('div.quote')

#         item = SpidermanItem()  # 实例化item类

#         for v in mingyan:  # 循环获取每一条名言里面的：名言内容、作者、标签
#             item['cont'] = v.css('.text::text').extract_first()  # 提取名言
#             tags = v.css('.tags .tag::text').extract()  # 提取标签
#             item['tag'] = ','.join(tags)  # 数组转换为字符串
#             yield item  # 把取到的数据提交给pipline处理

#         next_page = response.css(
#             'li.next a::attr(href)').extract_first()  # css选择器提取下一页链接
#         if next_page is not None:  # 判断是否存在下一页
#             next_page = response.urljoin(next_page)
#             # 提交给parse继续抓取下一页
#             yield scrapy.Request(next_page, callback=self.parse)
