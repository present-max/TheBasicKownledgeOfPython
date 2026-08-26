#字典：键值对存储方式，键唯一（只能是不可变类型int,str, tuple,float），值可重复，可修改
dict1={"name":"张三","age":18,"sex":"男"}
print(dict1)
print(dict1["name"])
print(dict1.get("age"))
dict1["name"]="李四"
#定义空字典
dict2={}
print(dict2)
#添加，修改，若键存在则修改，不存在则添加
dict2["name"]="张三"

