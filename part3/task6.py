class A:

    def send():
        pass

A.attr = 5
a = A()
print(a.attr in a.__dict__)
print(A.send())