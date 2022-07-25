# -*- coding: utf-8 -*-

# Define your item pipelines here
# 对收集到的item进行处理
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline


class BilibiliPipeline(object):
    def process_item(self, item, spider):
        return item


class Mp4FilesPipline(FilesPipeline):

    # 从item中取出分段视频的url列表并下载文件
    def get_media_requests(self, item, info):
        id = item['bvid']
        heads1 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'referer': f'https://www.bilibili.com/video/{id}?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6'
        }
        mp4_urls = item['mp4_urls']
        yield Request(mp4_urls, meta={'item': item}, headers=heads1)
        # for url in mp4_urls:
        #     yield Request(url=url, meta={'item': item, 'index': mp4_urls.index(url)})

    # 自定义分段视频下载到本地的路径(以及命名), 注意该路径是 FILES_STORE 的相对路径
    def file_path(self, request, response=None, info=None):
        title = request.meta['item']['title']
        # index = request.meta['index']  # 获取当前分段文件序号
        return "/%s.mp4" % title  # 返回路径及命名格式

    # 下载完成后, 将分段视频本地路径列表(FILES_STORE + 相对路径)填入到 item 的 file_paths
    def item_completed(self, results, item, info):
        item['mp4_paths'] = [self.store.basedir + x['path'] for ok, x in results if ok]
        return item


class Mp3FilesPipline(FilesPipeline):

    # 从item中取出分段视频的url列表并下载文件
    def get_media_requests(self, item, info):
        id = item['bvid']
        heads1 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'referer': f'https://www.bilibili.com/video/{id}?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6'
        }
        mp3_urls = item['mp3_urls']
        yield Request(mp3_urls, meta={'item': item}, headers=heads1)
        # for url in mp3_urls:
        #     yield Request(url=url, meta={'item': item, 'index': mp3_urls.index(url)})

    # 自定义分段视频下载到本地的路径(以及命名), 注意该路径是 FILES_STORE 的相对路径
    def file_path(self, request, response=None, info=None):
        title = request.meta['item']['title']
        # index = request.meta['index']  # 获取当前分段文件序号
        return "/%s.mp3" % title  # 返回路径及命名格式

    # 下载完成后, 将分段视频本地路径列表(FILES_STORE + 相对路径)填入到 item 的 file_paths
    def item_completed(self, results, item, info):
        item['mp3_paths'] = [self.store.basedir + x['path'] for ok, x in results if ok]
        return item
