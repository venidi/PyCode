# -*- coding:utf-8 -*-
import re
import time
import urllib.request as req
from bs4 import BeautifulSoup

# url = 'https://www.baidu.com'
# url = r'https://www.jianshu.com'
url = r'https://www.zhihu.com/question/27830729'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
           }
page = req.Request(url, headers=headers)
page_info = req.urlopen(page).read().decode('utf-8')

soup = BeautifulSoup(page_info, 'html.parser')
# titles = soup.find_all('a', 'title')

links = soup.find_all('img', "origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))
# print(soup)
local_path = r'e:\sppic'

for link in links:
    print(link.attrs['src'])
    req.urlretrieve(link.attrs['src'], local_path + r'\%s.jpg' % time.time())
# for title in titles:
#     print(title.string)
#
# try:
#     file = open(r'e:\title.txt', 'w')
#     for title in titles:
#         file.write(title.string + '\n')
# finally:
#     if file:
#         file.close()