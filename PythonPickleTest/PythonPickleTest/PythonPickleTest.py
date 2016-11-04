import pickle

class MyFirstClass(object):
    
    def __init__(self):
        self.arg1 = 42
        self.arg2 = 44

    def show(self):
        print('this is {}, arg1={}, arg2={}'.format(self, self.arg1, self.arg2))

class MySecondClass(object):

    def __init__(self, first_class):
        self.arg1 = 88
        self.first_class = first_class

    def show(self):
        print('this is {}, arg1={}, first_class={}'.format(self, self.arg1, self.first_class))
        self.first_class.show()

    def get_first(self):
        return self.first_class

def main():
    
    first = MyFirstClass()
    second = MySecondClass(first)
    print(first, second)
    first.show()
    second.show()

    # pickle these objects, the first object will only be pickled once
    pickle_file = open('picklefile.pkl', 'wb')
    pickle.dump((first, second), pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle_file.close()

    # Forget them
    first = None
    second = None
    print(first, second)

    # Now load them back from the pickle file
    pickle_file = open('picklefile.pkl', 'rb')
    (first, second) = pickle.load(pickle_file)
    pickle_file.close()

    # And now load a second set from the same pickle file
    pickle_file = open('picklefile.pkl', 'rb')
    (third, fourth) = pickle.load(pickle_file)
    pickle_file.close()

    # Check we have restored the references
    print(first, second)
    first.show()
    second.show()
    assert(second.get_first() == first)     # second's first object should be the same as first

    print(third, fourth)
    third.show()
    fourth.show()
    assert(fourth.get_first() != first)     # fourth's first object should not be the same as first

    print('done')


if __name__ == "__main__":
    main()