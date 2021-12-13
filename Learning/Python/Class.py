class myclass1:
    x = 5
    y = 10
    def func1(self):
    
        print('in func1 in myclass1')
        print('x',self.x)
        print('y',self.y)

    def func2(self):
        print('in func2 in myclass1')
        print('x*y',self.x*self.y)
        print('x/y',self.x/self.y)

    def func3(self, arg1 , arg2):
        print('in func3 in myclass1')
        print('your age is: ', arg2)
        print('your name is: ', arg1)

class myclass2(myclass1):
    def func(self):
        print('in func in myclass2')
        self.func1()
        self.func2()
        self.func3('ahmed','22')
    











# def main():
#     cls = myclass()
#     print(cls.x)
#     print(cls.y)
#     cls.func1()
#     cls.func2()


# if __name__ == '__main__': main()