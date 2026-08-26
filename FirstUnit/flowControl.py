#条件运算符
score=700
#if elif else后的代码块要在前面缩进（tab）相当于四个空格键
if(score > 680):
    print("我就去读清华")
    print("走上人生巅峰")
elif(score > 600 and score < 680):
    print("勉强接受")
    print("以后发奋图强")
else:
    print("我就回去复读")
    print("从此卧薪尝胆")
#匹配运算符
day = 7
match day:
    case 1:print("今天星期一")
    case 2:print("今天星期二")
    case 3:print("今天星期三")
    case 4:print("今天星期四")
    case 5:print("今天星期五")
    case 6|7:print("今天周末")
    case _:print("输入有误")
#循环运算符
count=10
while count>0:
    print(f"倒计时{count}")
    count-=1
else:#可有可无
    print("循环正常结束")

str="hello world!"
for s in str:
    print(s)
else:
    print("遍历结束")
#range:左开右闭，步长
for s in range(1,11,1):
    print(s)