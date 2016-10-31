# Simple Python yield example

val = 0

def yield_func(max):
    """This is a generator function
       - each time it is called it will return a value back until the max value is reached
       - it then throws a StopIteration exception (either when a 'return' statement is 
       - encountered, or when execution reaches an implicit return)
    """
    global val
    while val < max:
        yield val
        val += 1

    print('nope')

gf = yield_func(6)
try:
    print(gf.__next__()) #0
    print(gf.__next__())
    print(gf.__next__())
    print(gf.__next__())
    print(gf.__next__())
    print(gf.__next__()) #5
    print(gf.__next__()) # prints nope, throws StopIteration
    print(gf.__next__())
except StopIteration:
    print('Caught exception when val is {}'.format(val))

