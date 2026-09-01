class car:
    def __init__(self, color, brand, wheel):
        # 私有属性：__color：外部只能通过公有方法获取颜色
        self.__color = color
        self.brand = brand
        self.wheel=wheel

    def charge(self):
        print("补充燃料的方法：")

    def run(self):
        print("正在运行")
    def get_color(self):#抽象方法
        pass

class fuelcar(car):
    def __init__(self, color, brand, wheel, fueltype):
        #调用父类的构造方法
        super().__init__(color, brand, wheel)
        self.fueltype = fueltype
    def charge(self):#重写父类方法
        print("补充燃料的方法：", self.fueltype)

class elecar(car):
    def __init__(self, color, brand, wheel, battery):
        super().__init__(color, brand, wheel)
        self.battery = battery
    def charge(self):#重写父类方法
        print("补充燃料的方法：", self.battery)

class aidriver:
    def __init__(self, name):
        self.name = name

# 多继承
class xiaomica(car, aidriver):
    pass

#方法执行顺序是先找当前类的方法，如果找不到再找继承的第一个父类的方法
xiaomica = xiaomica("red", "xiaomi", 4)

