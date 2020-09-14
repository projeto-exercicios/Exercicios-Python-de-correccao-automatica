import random
from random import seed
from random import choice
from random import randint
from string import ascii_letters

seed(1885716)


z = []
for i in range(19000):
    z.append(choice((randint(0,410), choice(ascii_letters))))


def str_int_splitter(List):
    return [j for j in List if isinstance(j, str)],           [j for j in List if isinstance(j, int)]


def create_dict(str_z, int_z):
    l = {}
    size_str_a = len(str_z)
    size_int_a = len(int_z)
    for i in range(size_str_a):
        if i < size_str_a:
            l[str_z[i]] = int_z[i % size_int_a]
        else:
            l[str_z[i]] = ''
    return l

def get_max_key():

def get_min_key():

class Dictionary:

    def __init__(self, dictionary):
        self.l = dictionary

    def __getitem__(self, var):
        if isinstance(var, str):
            return [value for key, value in self.l.items() if key == var]
        if isinstance(var, int):
            return [key for key, value in self.l.items() if value == var]
        else: return "None"

    def __setitem__(self, key, value):
        self.l[key] = value
        

str_z, int_z = str_int_splitter(z)
l = create_dict(str_z, int_z)
f = Dictionary(l)
