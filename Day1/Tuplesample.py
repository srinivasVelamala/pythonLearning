import sys

a_list = list()
a_tuple = tuple()

a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)

print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

print(f'list values--', a_list)
print(f'tuple values--', a_tuple)

tup = ('b','a','n','a','n')
print(f'Tuple count --', tup.count('a'))
