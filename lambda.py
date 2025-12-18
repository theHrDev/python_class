# SINGLE PARAMETER
a = lambda val : val *2
print(a(2))

# MULTIPLE PARAMETER
mul = lambda val, num : val * num
print(mul(3,4))

# LAMBDA METHOD (MAP AND FILTER)

# MAP METHOD -- map through an iterable data type(tuple,string,list) - it behaves like for loop sometimes
result = list(map(lambda name : len(name) >= 5,  ["Tade","Tunde","Dotun"]))
print(result) # [False, True , True]

nums = range(1,11)
res = list(map(lambda num : num * 2 , nums))
print(res)

res = tuple(map(lambda val: val > 7, [5, 8, 2, 15]))
print(res)


# FILTER METHOD -- return the element that match the condition
result = list(filter(lambda name : len(name) >= 5,  ["Tade","Tunde","Dotun"]))
print(result)

# CHAINING METHOD -- using both map and filter for a question
names = ["Tolu", "Ojo", "Abidakun", "Alekuwodo", "abcdef"]
result = filter(lambda name: len(name) > 5, names)
res = list(map(lambda identity : len(identity), result))
print(res)