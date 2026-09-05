#定义装饰器，在各种操作前进行登录校验
def login_check(func):
    def wrapper():
        print("正在登录...")
        return func()
    return wrapper

#定义写评论的函数
@login_check#语法糖式调用方法，调用被装饰函数就相当于调用wrapper函数
def write_comment():
    print("正在写评论...")

#传统方式的调用方法
function=login_check(write_comment)#这里就是接受返回的wrapper函数
function()

