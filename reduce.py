import collections
from functools import reduce
import functools
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
# print("--------")

names_and_ages = tuple(
    {'name': x.name, 'age': 2022-x.born}
    for x in scientists
)
#pprint(names_and_ages)
'''Now we want to calculate the total age, for that we use the reduce function'''

# total_age = reduce(
#     lambda acc, val: acc+val['age'],
#     names_and_ages,0

#)
#print(total_age)
'''I could also do'''
# my_sum = sum(x['age']for x in names_and_ages)
# print(my_sum)

'''Another thing we could do, is grouping scientists by field'''
#{'physics':[],'chemistry':[],'biology':[],'engineering':[]}


def reducer(acc,val):
    acc[val.field].append(val.name)
    return acc

scienists_by_field = reduce(
    reducer,
    scientists,
    {'physics':[],'chemistry':[],'biology':[],'engineering':[]}


)

pprint(scienists_by_field)

sci_by_field = functools.reduce(
    lambda acc, val: {**acc, **{val.field: acc[val.field]+[val.name]}},
    scientists,
    {'physics':[],'chemistry':[],'biology':[],'engineering':[]}

) 
print('-----')
pprint(sci_by_field)












