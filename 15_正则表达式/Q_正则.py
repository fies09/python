#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
正则匹配,匹配日期2018-03-20

url='https://sycm.taobao.com/bda/tradinganaly/overview/get/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462/'

'''
import re

s = "url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462/'"
#提取一段特征语句用(.*?)匹配即可
# result = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)
result = re.findall("[0-9]*-[0-9]*-[0-9]*",s)

print(result)