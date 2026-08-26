#无序（不能通过索引访问元素），不重复，可变
set1={1,2,3,4,5}
print(set1)
#定义空集合
set2=set()
print(set2)
#随机删除元素并返回
set1.pop()
#求差集-
set3={1,2,3,4,5,6,7,8,9,10}
set4={1,2,3,4,5,6}
print(set3.difference(set4))
#求交集&
print(set3.intersection(set4))
#求并集|
print(set3.union(set4))
#集合推导式
set5={i for i in range(1,11)}
#不可切片

