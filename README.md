# flatten
sample python function to flat a list of sublist recursively

### How to use

Giving a list with sublists ([[1,2,[3]],4]) the method return a flattened version ([1,2,3,4]).

### Notes
The problem could to be resolved easly with a recursive approach.

```python
def flatten(elements):
    # stop if elements is empty
    if not elements:
        return elements

    # check if current element is an istance of list
    if isinstance(elements[0], list):
        # divide solution in two subs
        return flatten(elements[0]) + flatten(elements[1:])

    return elements[:1] + flatten(elements[1:])
```
