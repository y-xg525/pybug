# Author:You
# @Time :2020/8/27 17:46
# @Author:yxg
# @File :bsb.py
# @software: PyCharm

import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    page_text = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul >li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.text
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        detail_text = requests.get(url=detail_url,headers=headers).text
        detail_soup = BeautifulSoup(detail_text,'lxml')
        detail = detail_soup.find('div',class_='chapter_content').text
        fp.write(title+':'+detail+'\n')
        print(title,'保存成功')