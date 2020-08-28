# Author:You
# @Time :2020/8/28 14:21
# @Author:yxg
# @File :xpathtup.py
# @software: PyCharm

import requests
from lxml import etree
import os
if __name__ == "__main__":
    if not os.path.exists('./tupian'):
        os.mkdir('tupian')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'http://pic.netbian.com/4kmeinv/'
    response = requests.get(url=url,headers=headers)
    # response.encoding='utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    for li in li_list:
        plist = li.xpath('./a/img/@src')[0]
        pexp = li.xpath('./a/img/@alt')[0]+'.jpg'
        p_url = 'http://pic.netbian.com'+plist
        # 单独对乱码的部分进行设定
        pexp = pexp.encode('iso-8859-1').decode('gbk') #重新赋值
        # print(plist, pexp)
        pic_page = requests.get(url=p_url,headers=headers).content
        pic_path = 'tupian/'+pexp
        with open(pic_path,'wb') as fp:
            fp.write(pic_page)
            print(pexp,'保存成功')


