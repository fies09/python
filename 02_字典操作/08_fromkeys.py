#coding = utf-8
'''
    标题 fromkeys
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
fromkeys用法
'''
v = dict.fromkeys(['k1','k2'],[])   #{'k1':[],'k2':[]}
# v['k1'].append(666)
# print(v)    #{'k1': [666], 'k2': [666]}
# v['k2'] = 888
# print(v)    #{'k1': [666], 'k2': 888}

#id()函数,获取内存地址
print(id(v['k1']))
print(id(v['k2']))