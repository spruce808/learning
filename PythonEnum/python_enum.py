# Simple Python enum example

from enum import Enum

class Animals(Enum):
    dog = 1
    cat = 2
    rat = 3

for animal in Animals:
    print('Animal = {}: name={}: val={}'.format(animal, animal.name, animal.value))

print('Dog is {}'.format(Animals(1)))
print('Cat is {}'.format(Animals['cat']))

print('Cat is not a dog {}',format(Animals.cat == Animals.dog))
print('Cat is not 1 {}'.format(Animals.cat != 1))

val = 3
e = Animals.cat
print('Cat is not val {}'.format(e != val))

try:
    val = int(e)
    print('Val is {}'.format(val))
except TypeError:   
    # will fail here - use IntEnum class instead
    pass
