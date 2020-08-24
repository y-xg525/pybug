#-*- encoding='utf-8' -*-
#@Time : 2020/8/23 20:14
#@Author : you
#@File : pic.py
#@software : PyCharm

import requests
if __name__ == "__main__":
    url = 'https://pic.qiushibaike.com/system/pictures/12349/123498358/medium/9D2GFWM4NPUZC1OL.jpg'
    #text:字符串  json():对象   content:二进制
    imag_data = requests.get(url=url).content

    with open('qiutu.jpg','wb') as fp:
        fp.write(imag_data)