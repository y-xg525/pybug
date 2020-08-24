#-*- encoding='utf-8' -*-
#@Time : 2020/8/20 16:21
#@Author : you
#@File : baiduts.py
#@software : PyCharm
import requests
import json
if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'  # post请求，找关键字
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
        }  # UA反爬
    kw = input('请输入关键字：')
    data = {'kw':kw}
    response = requests.post(url=post_url,data=data,headers=headers)
    # json类型返回obj,确定返回响应数据类型为json才可使用
    dict_obj = response.json()
    #存储
    filename = kw+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False) #include Chinese
    print('over')