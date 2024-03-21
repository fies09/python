#coding = utf-8
'''
    14,字典根据键从小到大排序dict = {'name':'zs','age':18,'city':'深圳','tel':'1362626627'}
'''
dict = {'name':'zs','age':18,'city':'深圳','tel':'1362626627'}
# print('排序后的结果为:',sorted(dict.items(),key=lambda e:e[0]))    #升序,从小到大
#扩展,降序,从大到小,reverse=False升序,(不写)默认是升序,添加reverse=True参数降序,e[0]:按键  e[1]按值排序
print('排序后的结果为:',sorted(dict.items(),key=lambda e:e[0],reverse=True))
#扩展:按值升序
# print('排序后的结果为:',sorted(dict.items(),key=lambda e:e[1])) #报错.因为类型必须一致

