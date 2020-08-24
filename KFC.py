#-*- encoding='utf-8' -*-
#@Time : 2020/8/22 21:00
#@Author : you
#@File : KFC.py
#@software : PyCharm

import requests
if __name__ == "__main__":
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
               }

    kw = input('请输入关键字：')
    param = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=post_url,data=param,headers=headers)
    list_case = response.text
    filename = kw+'.txt'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(list_case)
    print(filename,'保存成功')




