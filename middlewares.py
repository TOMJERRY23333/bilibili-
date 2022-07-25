# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BilibiliSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BilibiliDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# class IPProxyMiddleware(object):
#
#     def fetch_proxy(self):
#         import random
#         import requests
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'}
#         # You need to rewrite this function if you want to add proxy pool
#         # the function should return a ip in the format of "ip:port" like "12.34.1.4:9090"
#         ip_pool = ['120.196.188.21:9091',
#                    '116.21.120.226:808',
#                    '121.13.252.61:41564',
#                    '61.145.1.181:7890',
#                    '113.90.178.118:7890',
#                    '183.240.203.136:8118',
#                    '113.104.133.6:8118',
#                    '14.29.139.251:8123',
#                    '39.108.101.55:1080',
#                    '103.59.176.154:8080',
#                    '163.142.146.241:8118',
#                    '27.45.184.180:8118',
#                    '120.197.179.166:8080',
#                    '210.5.10.87:53281',
#                    '103.59.39.74:8080',
#                    '59.38.60.118:9797',
#                    '58.251.98.105:3129',
#                    '120.237.144.77:9091',
#                    '39.108.156.112:8090',
#                    '121.13.252.62:41564',
#                    '183.239.62.251:9091',
#                    '121.13.252.60:41564',
#                    '39.108.56.233:38080',
#                    '27.46.44.166:9797',
#                    '106.75.171.235:8080',
#                    '183.236.232.160:8080',
#                    '119.122.212.20:9000',
#                    '116.21.121.2:808',
#                    '116.31.232.198:7890',
#                    '183.21.81.162:41825',
#                    '120.237.57.83:9091',
#                    '103.59.151.99:30001',
#                    '113.96.62.246:8081',
#                    '221.4.241.198:9091',
#                    '202.116.32.236:80',
#                    '113.118.134.249:9797']
#         for ip_port in ip_pool:
#             proxies = {'http': 'http://' + ip_port, 'https': 'https://' + ip_port}
#             try:
#                 res = requests.get('https://www.baidu.com', headers=headers,proxies=proxies)
#             except Exception:
#                 ip_pool.remove(ip_port)
#                 continue
#             if 200 <= res.status_code < 300:
#                 # 返回的状态码在200到300之间表示请求成功
#                 return ip_port
#             else:
#                 ip_pool.remove(ip_port)
#                 continue
#
#
#     def process_request(self, request, spider):
#         proxy_data = self.fetch_proxy()
#         if proxy_data:
#             current_proxy = f'http://{proxy_data}'
#             spider.logger.debug(f"current proxy:{current_proxy}")
#             request.meta['proxy'] = current_proxy
