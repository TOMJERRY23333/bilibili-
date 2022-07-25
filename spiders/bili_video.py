# coding:utf-8
"""
爬取b站热门视频
"""

import scrapy
from scrapy.http import Request
from scrapy import Selector, Spider
from scrapy.shell import inspect_response
import re
import json
from items import BilibiliItem


class BiliSpider(Spider):
    name = 'bilibili'
    scheme = 'https:'
    allowed_domain = ['bilibili.com']
    base_url = "https://www.bilibili.com"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
        'cookie': "buvid3=A0A8983E-1E54-145D-9747-45D1C809AA0D47567infoc; _uuid=98FD86E6-8911-26101-67DD-10B637743599547336infoc; i-wanna-go-back=-1; LIVE_BUVID=AUTO4216422314101026; rpdid=|(k|k)ku)l|J0J'uYRkkluJ~k; buvid4=E1852519-C9CF-A985-4042-5D719793ED1A80714-022013022-QpV8FfJYhXRnjhMekiBP2g%3D%3D; nostalgia_conf=-1; CURRENT_BLACKGAP=0; hit-dyn-v2=1; blackside_state=0; fingerprint=32b13a64ed4bb67189debe64caf0e0ee; buvid_fp_plain=undefined; DedeUserID=350014857; DedeUserID__ckMd5=59b5b7af523f6416; buvid_fp=87ffb5e3597a26608aed2b633ade9c51; b_ut=5; SESSDATA=76775d0c%2C1673944915%2C1c060%2A71; bili_jct=f79ff1039311065649dabc2ba0871960; sid=6h79j4jl; bsource=search_baidu; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; b_lsid=17A106E51_1822A372007; PVID=1; _dfcaptcha=d9d9fc490165d58ac50809e6b35a4850; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_A0A8983E%22%3A%221822A4F2F17%22%2C%22333.42.fp.risk_A0A8983E%22%3A%22181FC7966BB%22%2C%22333.999.fp.risk_A0A8983E%22%3A%22182245EE681%22%2C%22333.788.fp.risk_A0A8983E%22%3A%221822A4FD733%22%2C%22333.337.fp.risk_A0A8983E%22%3A%2218224FC9465%22%2C%22333.47.fp.risk_A0A8983E%22%3A%2218200B2F2DA%22%2C%22444.28.fp.risk_A0A8983E%22%3A%221821FE07649%22%2C%22333.934.fp.risk_A0A8983E%22%3A%221822A4F4F65%22%2C%22333.937.fp.risk_A0A8983E%22%3A%221821FE8B818%22%2C%22777.5.0.0.fp.risk_A0A8983E%22%3A%221821FE8D0B2%22%2C%22333.976.fp.risk_A0A8983E%22%3A%22182203F29BD%22%2C%22444.7.fp.risk_A0A8983E%22%3A%221822A4F1F7C%22%7D%7D; bp_video_offset_350014857=686028396243714000; innersign=0"
    }

    def start_requests(self):
        url = 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn='
        for i in range(1, 11):
            yield Request(url + str(i), callback=self.parse, headers=self.header)

    def parse(self, response):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'cookie': "buvid3=A0A8983E-1E54-145D-9747-45D1C809AA0D47567infoc; _uuid=98FD86E6-8911-26101-67DD-10B637743599547336infoc; i-wanna-go-back=-1; LIVE_BUVID=AUTO4216422314101026; rpdid=|(k|k)ku)l|J0J'uYRkkluJ~k; buvid4=E1852519-C9CF-A985-4042-5D719793ED1A80714-022013022-QpV8FfJYhXRnjhMekiBP2g%3D%3D; nostalgia_conf=-1; CURRENT_BLACKGAP=0; hit-dyn-v2=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1651840306; blackside_state=0; fingerprint=32b13a64ed4bb67189debe64caf0e0ee; buvid_fp_plain=undefined; DedeUserID=350014857; DedeUserID__ckMd5=59b5b7af523f6416; buvid_fp=87ffb5e3597a26608aed2b633ade9c51; theme_style=light; b_ut=5; SESSDATA=76775d0c%2C1673944915%2C1c060%2A71; bili_jct=f79ff1039311065649dabc2ba0871960; sid=6h79j4jl; bsource=search_baidu; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; bp_video_offset_350014857=685647853296549900; b_lsid=17A106E51_1822A372007; PVID=1; _dfcaptcha=d9d9fc490165d58ac50809e6b35a4850; innersign=1; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_A0A8983E%22%3A%221822A4F2F17%22%2C%22333.42.fp.risk_A0A8983E%22%3A%22181FC7966BB%22%2C%22333.999.fp.risk_A0A8983E%22%3A%22182245EE681%22%2C%22333.788.fp.risk_A0A8983E%22%3A%221822A4FD733%22%2C%22333.337.fp.risk_A0A8983E%22%3A%2218224FC9465%22%2C%22333.47.fp.risk_A0A8983E%22%3A%2218200B2F2DA%22%2C%22444.28.fp.risk_A0A8983E%22%3A%221821FE07649%22%2C%22333.934.fp.risk_A0A8983E%22%3A%221822A4F4F65%22%2C%22333.937.fp.risk_A0A8983E%22%3A%221821FE8B818%22%2C%22777.5.0.0.fp.risk_A0A8983E%22%3A%221821FE8D0B2%22%2C%22333.976.fp.risk_A0A8983E%22%3A%22182203F29BD%22%2C%22444.7.fp.risk_A0A8983E%22%3A%221822A4F1F7C%22%7D%7D"}
        self.logger.info('parse_0正在解析url:%s', response.url)
        # inspect_response(response, self)
        dic = json.loads(response.text)
        list = dic['data']['list']
        for i in list:
            item = BilibiliItem()
            item['title'] = i['title']
            item['author'] = i['owner']['name']
            item['coin'] = i['stat']['coin']
            item['bvid'] = i['bvid']
            item['dynamic'] = i['dynamic'].replace('\n', '')
            item['url'] = self.base_url + '/video/' + item['bvid']
            yield Request(item['url'] + '?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6', callback=self.parse_file,
                          meta={'item': item}, headers=headers)

    # def parse_1(self, response):
    #     self.logger.info('parse_1正在解析url:%s', response.url)
    #     item = response.meta['item']
    #     dic = json.loads(response.text)
    #     list = dic['data']['list']
    #     # url = 'https://www.bilibili.com/video/BV1kW4y117N6?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6'
    #
    #     for i in list:
    #         item['title'] = i['title']
    #         item['author'] = i['owner']['name']
    #         item['coin'] = i['stat']['coin']
    #         item['bvid'] = i['bvid']
    #         item['dynamic'] = i['dynamic'].replace('\n', '')
    #         item['url'] = self.base_url + '/video/' + item['bvid']
    #         # yield Request('https://www.bilibili.com/video/BV1Xa411M7jF?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6', callback=self.parse_file,
    #         #               meta={'item': item}, headers=headers)
    #         yield Request(item['url']+'?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6', callback=self.parse_file, meta={'item': item},headers=headers)

    def parse_file(self, response):
        # self.page += 1
        self.logger.info('parse_file正在解析url:%s', response.url)
        video = response.meta['item']
        url_str = response.xpath('//script[contains(text(),"window.__playinfo__")]/text()').extract()[0]
        # video['title'] = response.xpath('//h1/text()').extract()[0]

        video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', url_str)[0]
        audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', url_str)[0]
        video['mp4_urls'] = video_url
        video['mp3_urls'] = audio_url
        yield video
        # self.mp4_urls_list.append(video_url)
        # self.mp3_urls_list.append(audio_url)
        # if self.page < 190:
        #     self.logger.info('page = %s, 继续收集视频链接',self.page)
        # else:
        #     item['mp4_urls'] = self.mp4_urls_list
        #     item['mp3_urls'] = self.mp3_urls_list
        #     yield item
