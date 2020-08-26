#-*- encoding='utf-8' -*-
#@Time : 2020/8/26 10:05
#@Author : you
#@File : bs.py
#@software : PyCharm

if __name__ == "__main__":
    bs4数据解析原理：
    1.实例化一个BeautifulSoup对象，将页面源码数据加载到该对象中
    2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

    -from bs4 import  BeautifulSoup
    1.将本地的html文档中的数据加载到该数据：
        fp = open('./test.html','r',encoding='utf-8')
        soup = BeautifulSoup(fp,'lxml')
    2.将互联网上获取的页面源码加载到该对象中：
        page_text = response.text
        soup = BeautifulSoup(page_text,'lxml')