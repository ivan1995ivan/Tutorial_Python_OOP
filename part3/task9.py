class A:
    x = 4
    y = 2

    def dublicate(self):
        self.x = self.x
        self.y = self.y


a = A()
print(a.__dict__)
a.dublicate()
print(a.__dict__)