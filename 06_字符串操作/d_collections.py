#coding = utf-8
'''
    利用collections库的Counter方法统计字符串每个单词出现的次数
    str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahf;h"
'''
from collections import Counter
str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahf;h"
res = Counter(str)
print(res)