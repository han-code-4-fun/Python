import json
#this is to test json read and write


if "点赞数" == "点赞数":
	print('yes')
else:
	print('no')


def main():
	jsonStr = {
		"sandwich": "Reuben",
		"toasted": True,
		"toppings":[
			"Thousand Island Dressing",
			"Sauerkraut",
			"Pickles"],
		"price":8.99
	}
	print(type(jsonStr))
	#with open('testDict.json','w') as f:
	#	json.dump(jsonStr, f, indent=2)
	jsonStr['newKey_aweme_id']={'author_nickname':'Gary','desc':'一起来'}

	#print(jsonStr.get('name'))#get a none if key doesn't exist
	xyz = json.dumps(jsonStr, indent=2)#this makes it a string again
	print(type(xyz))
	print(xyz)
	print(jsonStr["toppings"][0])
	for ele in jsonStr["toppings"]:
		print(ele)


if __name__== "__main__":
	main()

#file_path = 'thelist.json'


