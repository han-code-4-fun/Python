import json

with open("testDict.json") as f:
	jsonData = json.load(f)
	#jsonData["car4"]["COLOR"] = "test"



jsonData["name"] = "William"
print(json.dumps(jsonData, ensure_ascii=False, indent=2))
jsonData["name"] = "Rocky"
print(json.dumps(jsonData, ensure_ascii=False, indent=2))



#None
if jsonData["car2"].get("sdasdw") != 'None':
	print('2222')
if jsonData["car2"].get("sdasdw") == 'None':
	print('333')

jsonData["car4"].update({"number":0})

print(json.dumps(jsonData, ensure_ascii=False, indent=2))


jsonData["car4"].update({"number":123})

print(json.dumps(jsonData, ensure_ascii=False, indent=2))

jsonData["car5"] = {"name":"car2go"}

aaa={"Car6":
		{
			"Tesla":"$45555"
		}
}

jsonData.update(aaa)
print(json.dumps(jsonData, ensure_ascii=False, indent=2))