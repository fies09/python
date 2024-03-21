#coding = utf-8
'''
字符串a = 'not 404 found 张三 99 深圳',每个词中间是空格,用正则过滤掉英文和数字,最终输出'张三 深圳'
'''
import re
a = 'not 404 found 张三 99 深圳'
# print(a)
# #以空格分隔字符串为列表
# b = a.split(' ')
# print(b)
# #正则匹配数字\d 和字符[a-zA-Z]
# res = re.findall('\d+|[a-zA-Z]+',a)
# print(res)
# #取出列表中不包含字符和数字的元素
# resu = [item for item in b if not item in res]
# # print(resu)
# #用join拼接字符串
# print(' '.join(resu))

# #逆向思维
# #以英文字符和数字作为分隔符
# b = re.split('[\d+|(a-z)+]',a)
# #得到空字符和中文的列表
# # print(b)
# # 用join进行拼接
#.strip()去掉头尾的空格
# print(''.join(b).strip())

'''
以下分别代表什么含义
    re.match():检查re是不是在String的开始位置匹配,只有在开始位置匹配成功才返回,不是在开始位置就返回None(多用于项目)
    eg:
        from django.http import HttpResponseBadRequest,HttpResponse        
        if not re.match(r'^1[3-9]\d{9}$',mobile):
            return HttpResponseBadRequest('请输入正确的手机号')
            # 2.2 验证密码是否符合规则
        if not re.match(r'^[a-zA-Z0-9]{8,20}$',password):
            return HttpResponseBadRequest('密码最少8位,最长20位')
    re.search():全局查找 匹配,会扫描整个字符串并返回第一个成功的匹配,
    re.compile()
    re.finditer()
    re.findall():按条件匹配
    re.sub():过滤
    re.split()
    re.subn()
'''
#re.sub过滤数字及字母
# print(' '.join(re.sub(r'[0-9a-zA-Z]','',a).split()))

#直接按中文匹配[\u4e00-\u9fa5]
#扩展:"\u4e00-\u9fa5"用来判断是不是中文的一种条件
# print(' '.join(re.findall(r'[\u4e00-\u9fa5]+',a)))

#最后一种
l = a.split()
print(l)
res = re.findall('\d+|[a-zA-Z]+',a)
print(res)
for i in res:
    if i in l:
        l.remove(i)
new_str = " ".join(l)
print(new_str)


'''
< div class=“nam”>中国< /div>，用正则匹配出标签里面的内容（“中国”），
其中class的类名是不确定的
'''
import re

str = "<div class = 'nam'>中国</div>"
res= re.findall("<div class = '.*'>(.*?)</div>",str)

print(res)