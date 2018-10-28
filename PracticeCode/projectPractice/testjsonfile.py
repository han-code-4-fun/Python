import json

def main():
#	jsonStr = '''{
#		"sandwich": "Reuben",
#		"toasted": true,
#		"toppings":[
#		"Thousand Island Dressing",
#		"Sauerkraut",
#		"Pickles"
#		],
#		"price":8.99
#	}'''
	with open('createdJson.json') as jsonStr:

		data = json.load(jsonStr)
		#print(type(jsonStr))
		print(type(data))

		print("Sandwich:" + data['sandwich'])
		if(data['toasted']):
			print("And it;s toasted!")
		for topping in data['toppings']:
			print("Topping:" + topping)

#	with open('createdJson.json','w') as f:
#		json.dump(data, f, indent=4)


if __name__== "__main__":
	main()

#file_path = 'thelist.json'

    #print(js.aweme_list[0].author.enterprise_verify_reason)

