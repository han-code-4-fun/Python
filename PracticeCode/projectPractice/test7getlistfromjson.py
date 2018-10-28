import json

with open('todayList.json',encoding='utf-8') as abc:
	data = json.load(abc)

print(type(data))
for each in data:
	print(each[1])

