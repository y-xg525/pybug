#-*- encoding='utf-8' -*-
#@Time : 2020/8/22 18:54
#@Author : you
#@File : douban.py
#@software : PyCharm

import requests
import json
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
        }
    response = requests.get(url=url,params=param,headers=headers)
    list_case = response.json()
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_case,fp=fp,ensure_ascii=False)

    print('保存成功')