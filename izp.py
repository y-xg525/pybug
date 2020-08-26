#-*- encoding='utf-8' -*-
#@Time : 2020/8/25 19:13
#@Author : you
#@File : izp.py
#@software : PyCharm

import requests
import re
import os
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    if not os.path.exists('./qiutulib'):
        os.mkdir('./qiutulib')
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pagenumb in range(1,3):
        new_url = format(url%pagenumb)
        page_text = requests.get(url=new_url, headers=headers).text

        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'#正则表达式获取图片链接
        imag_list = re.findall(ex,page_text,re.S)
        print(imag_list)
        for each in imag_list:
            each = 'https:'+each
            imag_page = requests.get(url=each,headers=headers).content
            # 图片命名
            imag_name = each.split('/')[-1]
            imag_path = './qiutulib/'+imag_name
            with open(imag_path,'wb') as fp:
                fp.write(imag_page)
                print(imag_name+'保存成功')

# <div class="thumb">
#
# <a href="/article/123503541" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12350/123503541/medium/P2AL142VYQHLDILA.jpg" alt="糗事#123503541" class="illustration" width="100%" height="auto">
# </a>
# </div>




