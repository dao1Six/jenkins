class A():

    @classmethod
    def outer(cls):
        x = 1
        def inner():
            y = x + 1
            print (y)
        print(inner)


if __name__ == '__main__':
    A.outer()