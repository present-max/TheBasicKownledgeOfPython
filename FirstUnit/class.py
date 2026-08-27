class stu:
    pass

#创建对象
s1=stu()
#动态添加属性
s1.name="zhangsan"
s1.age=18
print(s1.name,s1.age)
#将对象的属性已字典的形式打印出来
print(s1.__dict__)
print(s1)

class stu:
    #类属性：属于类
    teacher="HYC"

    #构造方法：self相当于java中的this
    def __init__(self,name,age):
        #实例属性：属于对象
        self.name=name
        self.age=age

    #实例方法
    def study(self):
        print(self.name,"正在学习")
    def sleep(self):
        print(self.name,"正在睡觉")

    #魔法方法
    #重写toString方法,输出对象名称不会输出地址值
    def __str__(self):
        return "stu类的实例对象，name:"+self.name+",age:"+str(self.age)
    #重写equals方法，比较两个对象是否相等
    def __eq__(self, other):
        return self.name==other.name and self.age==other.age
    #重写lessThan方法，比较两个对象的大小
    def __lt__(self, other):
        return self.age<other.age

s1=stu("zhangsan",18)
print(s1.name,s1.age)
s1.study()
s1.sleep()
print(s1)
print(s1==s1)
print(s1<s1)




