try:
    print(name)
except NameError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("无论是否发生异常都会执行")
