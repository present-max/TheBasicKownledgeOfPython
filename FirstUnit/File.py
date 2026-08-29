#打开文件
f=open("./resourse","r",encoding="utf-8")
#读取文件
string=f.read()
#关闭资源
f.close()

#文件操作模式，w:写(若文件存在则覆盖，不存在则创建)，r:读(只读,若文件不存在则报错)，a:追加
f=open("./resourseplus","w",encoding="utf-8")
f.write("hello world")
f.close()

#使用with语句打开文件,自动关闭资源
with open("./resourse","r",encoding="utf-8") as f:
    string1=f.read()
    print(string)
