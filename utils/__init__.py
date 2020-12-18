from random import randint

'''
method to flat a list with sublists
'''
def flatten(elements):
    # stop if elements is empty
    if not elements:
        return elements

    # check if current element is an istance of list
    if isinstance(elements[0], list):
        # divide solution in two subs
        return flatten(elements[0]) + flatten(elements[1:])

    return elements[:1] + flatten(elements[1:])

'''
method to generate a random list with sublists
'''
def random_list():
    return [[randint(0, randint(1,30)) for i in range(randint(1,10))] for n in range(randint(1,10))]