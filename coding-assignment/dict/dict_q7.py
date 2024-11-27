# Group a list of dictionaries by a common key

data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}, {'name': 'Eve', 'age': 30}]
grouped = {}
for item in data:
    key = item['age']
    grouped.setdefault(key, []).append(item)
print(grouped)
