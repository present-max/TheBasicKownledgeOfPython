#列表可以存储不同类型的变量
list=[1,2,3,4,5,5.5,"hello"]
print(list)
#列表中的元素获取
#正向索引
print(list[0])
#反向索引（获取倒数第一个元素）
print(list[-1])
#元素修改
list[-1]="world"
print(list)
#删除
del list[-2]
print(list)
#切片(起始索引，结束索引，步长)
print(list[0:5:1])
#合并列表
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
#方法一
LIST=list1+list2
#方法二(*代表解包操作，将列表拆成单个元素)
LIST1=[*list1,*list2]
#列表推导式(从一个列表中取出元素加入另一个列表)
num_list=[12,13,14,15]
new_list=[i**2 for i in num_list if i % 2==0]

#常见方法
#添加元素
list.append("hello")
#插入元素(在指定索引前插入)
list.insert(0,"world")
#删除元素
list.remove("world")
#判断元素是否在列表中
print("hello"in list)