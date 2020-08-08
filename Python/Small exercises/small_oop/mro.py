#ways to referece the mro given multiple inherited classes


# __mro__ attribute, for example Penguin.__mro__
#mro() method for example Penguin.mro()
# builtin help(cls) method for example help(Penguin)

class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Defined In: B")

class C(A):
    def do_something(self):
        print("Method Defined In: C")

class D(B, C):
    def do_something(self):
        print("Method Defined In: D")

thing = D()
print(thing.do_something())