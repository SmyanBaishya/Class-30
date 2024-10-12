class Computer():
    def __init__(self):
       self.__maxprice = 1200 

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice = price

x = Computer()
x.sell()
x.__maxprice = 1000
x.sell()
x.setmaxprice(1000)
x.sell()