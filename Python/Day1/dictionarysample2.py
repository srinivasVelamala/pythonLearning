dict1 = {
    "name": "Alice",
    "age": 20,
    "location": "hyd"
}
dict2 ={
    "name": "Rick",
    "age": 35,
    "location1": "banglore",
    "active": "true"
}
dict2.update(dict1)
print(f'AFter update dict1 with dict2', dict2)

try:
    print(dict1["active"])
except:
    print('No such key')
