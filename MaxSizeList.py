class MaxSizeList(object):

    def __init__(self,val):
        self.size = val
        self.count = 0
        self.limitedList = []

    def get_list(self):
        return self.limitedList

    def push(self,val):
        self.count+=1
        if self.count > self.size:
            self.limitedList.pop(0)
            self.count-=1
        self.limitedList.append(val)


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
 