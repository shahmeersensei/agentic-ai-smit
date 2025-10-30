"""OOP examples."""

class Person:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    p = Person('Alice')
    print(p.name)
