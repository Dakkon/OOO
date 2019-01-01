#also __init practice

class MyNum(object):
    def __init__(self,val):
        print('calling __init__')
        self.val=val

    def increment(self):
        self.val+=1


dd = MyNum(5)
dd.increment()
dd.increment()

print(dd.val)

print()
