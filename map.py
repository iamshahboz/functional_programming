'''Map function in python 
this is another built is function in python '''

import collections
Scientist = collections.namedtuple('Scientist',[
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name="Albert Einstein",field='physics',born=1879,nobel=True),
    Scientist(name="Marie Curie",field='chemistry',born=1867,nobel=True),
    Scientist(name="Isaac Newton",field='physics',born=1642,nobel=False),
    Scientist(name="Charles Darwin",field='biology',born=1809,nobel=False),
    Scientist(name="Nicola Tesla",field='engineering',born=1989,nobel=False),
    Scientist(name="Ada Lovelace",field='engineering',born=1815,nobel=False),
)

from pprint import pprint
#pprint(scientists)
''' we will use map, to trasform is
    we will take this list list and assamble to a new list that contained the names 
    ages of this scientists

'''
# names_and_ages = tuple(map(
#     lambda x: {"name": x.name,"age": 2022-x.born},scientists
# ))
# pprint(names_and_ages)

# we can do it with list comprehension as well
n_a = [{'name': x.name,'age':2021-x.born}
        for x in scientists]

pprint(tuple(n_a))
'''What we did down there it didn't modified the list at all, it took list as an
input and generated a new list'''




