import operator
class B:

    def add(self, x, y):
        return operator.add(x, y)

a = B()
print(a.add(15,27.1))


