# -*- coding:utf-8 -*-

import urllib.request as re

url = 'https://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
           }
page= re.Request(url, headers=headers)
page_info = re.urlopen(page).read().decode('utf-8')
print (page_info)