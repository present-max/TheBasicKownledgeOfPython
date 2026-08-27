#默认参数要放在最后
def stu(name,score,gender,age=19):
    #函数的说明文档
    """
    打印学生信息
    :param name:姓名
    :param score:分数
    :param gender:性别
    :param age:年龄
    :return:
    """
    print(f"name:{name},score:{score},gender:{gender},age:{age}")

#可变参数   *是位置传参封装为元组，**是关键字传参封装为字典
def caculate(*args,**kwargs):
    minnum=min(args)
    maxnum=max(args)
    avgnum=sum(args)/len(args)
    if kwargs.get("round") is not None:
        avgnum=round(avgnum,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"min:{minnum},max:{maxnum},avg:{avgnum}")
    return minnum,maxnum,avgnum

#匿名函数，这里的square是函数变量
cube=lambda x:x*x*x
print(cube(5))
#函数作为参数
num=3
def function(cube,num):
    return cube(num)
print(function(cube,num))



