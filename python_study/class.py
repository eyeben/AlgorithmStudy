class Infos:

    def func1():
        print("func1")

    def func2(self):
        print("func2")



test=Infos()
#Infos.func1()
#Infos.func2() <-X
#test.func1() <-X
#test.func2()


class mother():
    def __init__(self,hey):
        self.hey=hey
class sibling(mother):
    def __init__(self,hey,boi):
        super().__init__(hey)
        self.boi=boi

print("a")