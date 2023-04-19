class A:
    pass


class B:
    pass


a = A()
b = B()
print(isinstance(a, B), type(b) == A, sep='\n')
print(type(b)== B)
