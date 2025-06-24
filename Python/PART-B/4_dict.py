# 4. Demonstrate use of Dictionaries 
d = {'name': 'Manju', 'age': 21, 'course': 'BCA'}
d['grade'] = 'A'
print("After adding 'grade':", d)
d.update({'college': 'XYZ College'})
print("After update with {'college': 'XYZ College'}:", d)
print("Loop through all key-value pairs:")
for key, value in d.items():
    print(key, ':', value)
print("Access value using key", d['name'])
print("Get value for key 'age':", d.get('age'))
print("Number of items:", len(d))
print("All keys:", d.keys())
print("All values:", d.values())
print("All key-value pairs:", d.items())
print("Removed last item", d.popitem())
print("Removed 'age'->", d.pop('age'))
print("Clear dict:", d.clear())
print("Now dict:", d)