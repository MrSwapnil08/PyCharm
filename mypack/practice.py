#Write a Python code to merge two dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged) #{'a': 1, 'b': 3, 'c': 4}

#program to find common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common) #[3, 4]

# program to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

 #Python code to implement a function to flatten a nested list
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]

#Python code to implement a queue using collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1