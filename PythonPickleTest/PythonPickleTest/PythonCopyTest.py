import copy

class MyBaseObject(object):
    
    def __init__(self, value):
        self.value = value

    def show(self):
        print('This is {}, value={}'.format(self, self.value))

class MyClass(object):

    def __init__(self, value, base):
        self.value = value
        self.base = base

    def show(self):
        print('This is {}, value={}, base={}'.format(self, self.value, self.base))

    def get_base(self):
        return self.base


base1 = MyBaseObject(1)
first = MyClass(42, base1)
base2 = MyBaseObject(2)
second = MyClass(44, base2)

third = copy.copy(first)        # will copy references
fourth = copy.deepcopy(second)  # will copy everything

print(first, second, third, fourth)
first.show()
second.show()
third.show()
fourth.show()

assert(first.get_base() == third.get_base())    # both first and third should refer to the same base object
assert(second.get_base() != fourth.get_base())  # second and fourth will have independent base objects

