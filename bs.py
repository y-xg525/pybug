#-*- encoding='utf-8' -*-
#@Time : 2020/8/26 10:05
#@Author : you
#@File : bs.py
#@software : PyCharm

# if __name__ == "__main__":
#     bs4数据解析原理：
#     1.实例化一个BeautifulSoup对象，将页面源码数据加载到该对象中
#     2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
#
#     -from bs4 import  BeautifulSoup
#     1.将本地的html文档中的数据加载到该数据：
#         fp = open('./test.html','r',encoding='utf-8')
#         soup = BeautifulSoup(fp,'lxml')
#     2.将互联网上获取的页面源码加载到该对象中：
#         page_text = response.text
#         soup = BeautifulSoup(page_text,'lxml')
#
#     3.soup.targename   soup.div/a  #定位到标签第一次出现的位置
#       soup.find('div')  #等同于上
#       soup.find('div',class_/id/attr='song')
#       soup.find_all('a')  #返回符合要求的所有标签
#       select:
#       soup.select('.tang')
#       soup.select('.tang > ul > li > a')[0]
#       soup.select('.tang > ul a') #空格代表多个层级
#       soup.a.text/string/get_text #string只能获取标签直系文本，其他两个可以获取标签内所有
