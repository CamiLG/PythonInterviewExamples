""" Detemine if a list is sorted using a generator defined by comprehension"""

items1 = [6, 8, 19, 20, 23, 41, 49, 53, 60, 71]
items2 = [2, 23, 34, 12, 45, 56, 78, 89, 94, 97]

def is_sorted(itemList):
    return all(itemList[i] <= itemList[i+1] for i in range(len(itemList)-1))

print(is_sorted(items1))
print(is_sorted(items2))