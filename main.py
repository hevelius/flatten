from utils import *

def main():
    items = [[1,2,[3]],4]
    results = flatten(items)
    print(results)
    newlist = random_list()
    print(newlist)
    results = flatten(newlist)
    print(results)

if __name__ == "__main__":
    main()


