#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
选择结果:
    names1 = ['Amir','Barry','Chales','Dao']
    names2 = names1
    names3 = names1[:]
    names2[0] = 'Alice'
    names3[1] = 'Bob'
    sum = 0
    for ls in (names1,names2,names3):
        if ls[0] == 'Alice':
            sum+=1
        if ls[1] == 'Bob':
            sum+=10
    print(sum)
'''
names1 = ['Amir','Barry','Chales','Dao']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0

# names1
# names2:['Alice','Barry','Chales','Dao']
# names3:['Amir','Bob','Chales','Dao']
#sum:12

for ls in (names1,names2,names3):
    if ls[0] == 'Alice':
        sum+=1
    if ls[1] == 'Bob':
        sum+=10

# print(id(names1),id(names2))
print(sum)