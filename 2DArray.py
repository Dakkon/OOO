class TwoDArray(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.matrix = [[0 for x in range(self.width)] for y in range(self.height)]

    def set_value(self, w, h, value):
        try:
            self.matrix[w][h] = value
        except IndexError:
            print("Out of bounds error")

    def get_value(self, w, h):
        try:
            return self.matrix[w][h]
        except IndexError:
            print("Out of bounds error")

    def rm_value(self, w, h):
        try:
            self.matrix[w][h] = 0
        except IndexError :
            print("Out of bounds error")


if __name__ == '__main__':
    Neo = TwoDArray(3, 3)
    print(Neo.set_value(0, 0, 1))
    print(Neo.set_value(1, 0, 2))
    print(Neo.set_value(2, 0, 3))
    print(Neo.set_value(0, 1, 4))
    print(Neo.set_value(1, 1, 5))
    print(Neo.set_value(2, 1, 6))
    print(Neo.set_value(0, 2, 7))
    print(Neo.set_value(1, 2, 8))
    print(Neo.set_value(2, 2, 9))

    for x in range(0,3):
        for y in range(0,3):
            print(Neo.get_value(x,y))

