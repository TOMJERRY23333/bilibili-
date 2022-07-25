# -*- coding: utf-8 -*-

# Scrapy settings for bilibili project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bilibili'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bilibili (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    # 'middlewares.IPProxyMiddleware': 100,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
#     'cookie': "buvid3=A0A8983E-1E54-145D-9747-45D1C809AA0D47567infoc; _uuid=98FD86E6-8911-26101-67DD-10B637743599547336infoc; i-wanna-go-back=-1; LIVE_BUVID=AUTO4216422314101026; rpdid=|(k|k)ku)l|J0J'uYRkkluJ~k; buvid4=E1852519-C9CF-A985-4042-5D719793ED1A80714-022013022-QpV8FfJYhXRnjhMekiBP2g%3D%3D; nostalgia_conf=-1; CURRENT_BLACKGAP=0; hit-dyn-v2=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1651840306; blackside_state=0; fingerprint=32b13a64ed4bb67189debe64caf0e0ee; buvid_fp_plain=undefined; DedeUserID=350014857; DedeUserID__ckMd5=59b5b7af523f6416; buvid_fp=87ffb5e3597a26608aed2b633ade9c51; theme_style=light; b_ut=5; SESSDATA=76775d0c%2C1673944915%2C1c060%2A71; bili_jct=f79ff1039311065649dabc2ba0871960; sid=6h79j4jl; bsource=search_baidu; PVID=1; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; innersign=1; b_lsid=F9A4ADDF_18224FBB881; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_A0A8983E%22%3A%2218224C440FB%22%2C%22333.42.fp.risk_A0A8983E%22%3A%22181FC7966BB%22%2C%22333.999.fp.risk_A0A8983E%22%3A%22182245EE681%22%2C%22333.788.fp.risk_A0A8983E%22%3A%2218224F1AB0E%22%2C%22333.337.fp.risk_A0A8983E%22%3A%2218224FC9465%22%2C%22333.47.fp.risk_A0A8983E%22%3A%2218200B2F2DA%22%2C%22444.28.fp.risk_A0A8983E%22%3A%221821FE07649%22%2C%22333.934.fp.risk_A0A8983E%22%3A%2218224C470AA%22%2C%22333.937.fp.risk_A0A8983E%22%3A%221821FE8B818%22%2C%22777.5.0.0.fp.risk_A0A8983E%22%3A%221821FE8D0B2%22%2C%22333.976.fp.risk_A0A8983E%22%3A%22182203F29BD%22%7D%7D; bp_video_offset_350014857=685647853296549900"
# }

ITEM_PIPELINES = {'pipelines.Mp4FilesPipline': 1,'pipelines.Mp3FilesPipline': 2}
# 'scrapy.pipelines.files.FilesPipeline': None
# }

# FEED_URI='./%(name)s.csv' FEED_FORMAT='CSV' FEED_EXPORT_ENCODING='ansi'

FILES_STORE = './storage/data_4'
DOWNLOAD_MAXSIZE = 0
DOWNLOAD_WARNSIZE = 0
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'bilibili.middlewares.BilibiliDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bilibili.pipelines.BilibiliPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
