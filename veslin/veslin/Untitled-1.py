class demo():
    class_var = 0
    def init(self, var):
        demo.class_var +=1
        self.var = var
        print ('The Object value is:', var)
        print('The value of class variable is:', demo.class_var)
obj1 = demo(10)
obj2 = demo(20)
obj3 = demo(30)