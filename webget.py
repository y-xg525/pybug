#-*- encoding='utf-8' -*-
#@Time : 2020/8/19 20:56
#@Author : you
#@File : webget.py
#@software : PyCharm

import requests
if __name__ == "__main__":
    url = 'https://www.sogou.com/web'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
               }    # UA反爬
    kw = input('请输入关键字：')
    param = {'query':kw}
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    filename = kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'保存成功')
