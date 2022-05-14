'''Functional programming
it is programming style as OOP

It is a programming technique that avoids side effects in your program by performing computation
mainly though the evaluation of functions and it will rely heavily on immutable data 
structures

'''
#this example is mutable data structure
# scientists = [
#     {
#         'name':'Ada Lovelance','field':'math','born': 1815,'nobel':False
#     },
#     {
#         'name':'Ada Lovelance','field':'math','born': 1815,'nobel':False

#     },
#     {
#         'nime':'Ada Lovele','field':'math','born': 1815,'nobel':False

#     }
# ]
# print(scientists)
'''The problem with dictionaries is that, what is I make a typo, and instead of name, i
write nime, the program works because it will not check
and we don't want this'''

#what we will do instead

import collections
Scientist = collections.namedtuple('Scientist',[
    'name',
    'field',
    'born',
    'nobel',
])


#keep your data in tuple
scientists = (
    Scientist(name="Albert Einstein",field='physics',born=1879,nobel=True),
    Scientist(name="Marie Curie",field='chemistry',born=1867,nobel=True),
    Scientist(name="Isaac Newton",field='physics',born=1642,nobel=False),
    Scientist(name="Charles Darwin",field='biology',born=1809,nobel=False),
    Scientist(name="Nicola Tesla",field='engineering',born=1989,nobel=False),
    Scientist(name="Ada Lovelace",field='engineering',born=1815,nobel=False),

    
    


)

from pprint import pprint
pprint(scientists)
#now you can't do scientist[0].name = "Shahboz"











