from random import randint

def flatten(elements):
    # stop if elements is empty
    if not elements:
        return elements

    # check if current element is an istance of list
    if isinstance(elements[0], list):
        # divide solution in two subs
        return flatten(elements[0]) + flatten(elements[1:])

    return elements[:1] + flatten(elements[1:])