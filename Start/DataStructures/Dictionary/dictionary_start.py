# Example file for Programming Foundations: Algorithms by Joe Marini
# demonstrate dictionary usage


# TODO: create a dictionary all at once
dict = { 'name': 'John', 'age': 25, 'job': 'Developer' }
# print(dict)

# TODO: create a dictionary progressively
otherDict = {}
otherDict['name'] = 'John'
otherDict['age'] = 25
otherDict['job'] = 'Developer'
print(otherDict)

# TODO: replace an item
otherDict['age'] = 26
print(otherDict)

# TODO: try to access a nonexistent key
print(otherDict.get('salary', 'Not found'))


# TODO: iterate the keys and values in the dictionary
'''for key in otherDict.keys():
    print(key, otherDict[key])
'''
for key, value in otherDict.items():
    print(key, value)
