#-*- encoding='utf-8' -*-
#@Time : 2020/8/23 20:29
#@Author : you
#@File : zpic.py
#@software : PyCharm

import requests
import re
import os
if __name__ == "__main__":
    #创建一个文件夹存放图片
    if not os.path.exists('qiutulibs'):
        os.mkdir('qiutulibs')

    url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
        }
    page_text = requests.get(url=url, headers=headers).text

    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    imag_list = re.findall(ex, page_text, re.S) #re.S单行匹配，re.M多行匹配,findall:正则
    print(imag_list)
    for src in imag_list:
        src = 'https:' + src
        imag_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        imag_name = src.split('/')[-1]
        imag_path = 'qiutulibs/'+imag_name
        with open(imag_path,'wb') as fp:
            fp.write(imag_data)
            print(imag_name,'下载成功')







