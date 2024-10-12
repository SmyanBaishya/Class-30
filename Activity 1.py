class myclass():
    __privateVar = 2
    def __privMeth(self):
        print("I am inside class- myclass")

    def hello(self):
        print("Value of private variable is", myclass.__privateVar)


foo = myclass()
foo.hello()
foo.__privMeth