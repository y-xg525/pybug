# Author:You
# @Time :2020/8/28 15:30
# @Author:yxg
# @File :chengshi.py
# @software: PyCharm

import requests
from lxml import etree
if __name__ == "__main__":
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url, headers=headers).text
    # tree = etree.HTML(page_text)
    #
    # all_name = []
    # hot_li = tree.xpath('//div[@class="hot"]/div[2]/ul/li') #可用bottom,直系与非直系不同
    # all_li = tree.xpath('//div[@class="all"]/div[2]/ul/div[2]/li')
    # for li in hot_li:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     # print(hot_city_name)
    #     all_name.append(hot_city_name)
    #
    # for li in all_li:
    #     all_city_name = li.xpath('./a/text()')[0]
    #     all_name.append(all_city_name)
    # print(all_name,len(all_name))

    #统一编写
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_name = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_name.append(city_name)
    print(all_city_name,len(all_city_name))






