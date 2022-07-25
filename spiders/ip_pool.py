# # coding:utf-8
# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import random
#
# ROOT_URL = 'http://www.89ip.cn/index_'
#
# ip_list = []
# useful_ip = []
#
#
# def judge(ip_port):
#     heads ={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#     }
#     proxies = {'http': 'http://'+ip_port, 'https': 'https://'+ip_port}
#     try:
#         res = requests.get('https://www.baidu.com', headers=heads, proxies=proxies)
#         print(res)
#     except Exception:
#         return False
#     else:
#         if 200 <= res.status_code < 300:
#             # 返回的状态码在200到300之间表示请求成功
#             return True
#         else:
#             print('请求失败')
#             return False
#
#
# # 第三步：从ip_list中随机获取一个ip
# def get_random_ip():
#     print(ip_list)
#     while ip_list:
#         ip_port = random.choice(ip_list)
#         result1 = judge(ip_port)
#
#         if result1 is not False:
#             proxies = {'http': 'http://'+ip_port, 'https': 'https://'+ip_port}
#             useful_ip.append(proxies)
#             # return proxies
#         else:
#             ip_list.remove(ip_port)
#     # return None
#     return useful_ip
#
#
# class IpPool(object):
#
#     def _get_ip(self, n):
#         try:
#             headers = {'User-Agent': UserAgent.random}
#         except AttributeError:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                               'AppleWebKit/537.36 (KHTML, like Gecko) '
#                               'Chrome/84.0.4147.105 Safari/537.36 '}
#         url = ROOT_URL + '{page}.html'.format(page=n)
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         items = soup.find_all('td')
#         for i, j in zip(items[::5], items[1::5]):
#             ip_port = i.text.replace('\t', '').replace('\n', '') \
#                       + ':' + j.text.replace('\n', '').replace('\t', '')
#             ip_list.append(ip_port)
#
#     def run(self):
#         for x in range(1, 20):
#             self._get_ip(x)
#         return get_random_ip()
#
# if __name__ == '__main__':
#     ip = IpPool()
#     print(ip.run())