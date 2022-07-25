# import requests
# from lxml.html import etree
# import re
# # from spiders.ip_pool import IpPool
#
# url = 'https://www.bilibili.com/video/BV1ZB4y1Y7Hm?spm_id_from=333.934.0.0&vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6'
# heads ={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
# 'cookie':"buvid3=A0A8983E-1E54-145D-9747-45D1C809AA0D47567infoc; _uuid=98FD86E6-8911-26101-67DD-10B637743599547336infoc; i-wanna-go-back=-1; LIVE_BUVID=AUTO4216422314101026; rpdid=|(k|k)ku)l|J0J'uYRkkluJ~k; buvid4=E1852519-C9CF-A985-4042-5D719793ED1A80714-022013022-QpV8FfJYhXRnjhMekiBP2g%3D%3D; nostalgia_conf=-1; CURRENT_BLACKGAP=0; hit-dyn-v2=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1651840306; blackside_state=0; fingerprint=32b13a64ed4bb67189debe64caf0e0ee; buvid_fp_plain=undefined; DedeUserID=350014857; DedeUserID__ckMd5=59b5b7af523f6416; buvid_fp=87ffb5e3597a26608aed2b633ade9c51; theme_style=light; b_ut=5; SESSDATA=76775d0c%2C1673944915%2C1c060%2A71; bili_jct=f79ff1039311065649dabc2ba0871960; sid=6h79j4jl; bsource=search_baidu; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; bp_video_offset_350014857=685647853296549900; b_lsid=17A106E51_1822A372007; PVID=1; _dfcaptcha=d9d9fc490165d58ac50809e6b35a4850; innersign=1; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_A0A8983E%22%3A%221822A4F2F17%22%2C%22333.42.fp.risk_A0A8983E%22%3A%22181FC7966BB%22%2C%22333.999.fp.risk_A0A8983E%22%3A%22182245EE681%22%2C%22333.788.fp.risk_A0A8983E%22%3A%221822A4FD733%22%2C%22333.337.fp.risk_A0A8983E%22%3A%2218224FC9465%22%2C%22333.47.fp.risk_A0A8983E%22%3A%2218200B2F2DA%22%2C%22444.28.fp.risk_A0A8983E%22%3A%221821FE07649%22%2C%22333.934.fp.risk_A0A8983E%22%3A%221822A4F4F65%22%2C%22333.937.fp.risk_A0A8983E%22%3A%221821FE8B818%22%2C%22777.5.0.0.fp.risk_A0A8983E%22%3A%221821FE8D0B2%22%2C%22333.976.fp.risk_A0A8983E%22%3A%22182203F29BD%22%2C%22444.7.fp.risk_A0A8983E%22%3A%221822A4F1F7C%22%7D%7D"
# }
# # ip_pool = IpPool()
# # ip_port = ip_pool.run()
# res = requests.get(url,headers=heads)
# # print(res.text)
# tree = etree.HTML(res.text)
# url_str = tree.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
# video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"',url_str)[0]
# audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"',url_str)[0]
# heads1 = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
#     'referer':'https://www.bilibili.com/video/BV19g411o7d1?vd_source=65aa9381fce2b80aa78e4f2be0b3e7c6'
# }
#
# res1 = requests.get(video_url,headers=heads1)
# res2 = requests.get(audio_url,headers=heads1)
# print(res1,res2)
# with open('vedio.mp4','wb') as f:
#     f.write(res1.content)
# with open('audio.mp3','wb') as f:
#     f.write(res2.content)
#
# print(audio_url)
