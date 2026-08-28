#打开文件
f=open("./resourse","r",encoding="utf-8")
#读取文件
string=f.read()
#关闭资源
f.close()

f=open("./resourseplus","w",encoding="utf-8")
f.write("hello world")
f.close()

#使用with语句打开文件,自动关闭资源
with open("./resourse","r",encoding="utf-8") as f:
    string1=f.read()
    print(string)
