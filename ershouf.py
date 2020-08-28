# Author:You
# @Time :2020/8/28 13:47
# @Author:yxg
# @File :ershouf.py
# @software: PyCharm

import requests
from lxml import etree
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')

    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        fp.write(title+'\n')


