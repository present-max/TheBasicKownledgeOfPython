#元组一旦定义，不可修改
tuple=(1,2,3,4,5)
tuple1=1,2,3,4,5
print(tuple)
#元组的索引和切片
print(tuple[0])
print(tuple[1:3])
#元组不可变，不能修改元组中的元素
#元组的长度
print(len(tuple))
#元组的遍历
for i in tuple:
    print(i)
#元组的判断
print(1 in tuple)
#元组的索引
print(tuple.index(1))
#元组的计数
print(tuple.count(1))
#定义单元素元组
tuple=(1,)
print(tuple)
#元组的解包
t1=(1,2,3,4,5)#这里相当于组包
a,b,c,d,e=t1#将元组t1中的元素解包赋值给变量a,b,c,d,e
print(a,b,c,d,e)
first,second,*other,last=t1
print(first,second,other,last)
#组包与解包的理解
a=200
b=100
a,b=b,a
#c=100,200 组包
#a,b=c     解包
print(a,b)








