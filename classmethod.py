class A:
    x = 5
    y= 2
    def add(self, a,b):
        return a+b


instance = A()
A.add = classmethod(A.add)
print(A.add(5,3))