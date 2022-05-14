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
#new_list = filter(lambda x: x.nobel is False, scientists )
#another_one = filter(lambda x: x.born >1970,scientists)


'''lambda is one line, anonymus function, you can put  arguments and then you have
one expression  that gets evaluated, you don't have to do return
When we try to print(new_line), we will get a filter object which is iterable
Then we can iterate over it, and get the items'''

"""There is a question why we don't use just a loop,
for x in scientists:
    if x.nobel is True:
        print(x)

we will get the same result, that way is much more cleaner, our aim is to write a clean code

"""
# for i in another_one:
#     pprint(tuple(i))


#we have another thing it is list comprehension
#it is a replacement for filter function
a = [x for x in scientists if x.nobel is False]
pprint(tuple(a))

















