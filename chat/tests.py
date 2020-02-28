class A:
    def ong(self,a):
        self.a=a
        print("junaid")
class B(A):
    def ong(self,a):
        self.a=a
        print("khan")
class C(B,A):
    def ong(self,c):
        self.c=c
        print("marvellous")
x=C()
x=B()
x=A()
x.ong('b')
x.ong('a')
x.ong('c')

def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
x=add(5,6,1)
