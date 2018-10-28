import json,random

position=[]

randomList = []

for x in range(30):
	randomList.append(random.randint(1,50))


print(randomList)

def larggestPosition(inputList):#get 10 largest number's position in a list
	listOriginal = inputList.copy()
	listForBigNum = []
	listOfPosition=[]
	count = 0
	while count<10:
		big = 0
		for each in inputList:
			if each > big:
				big = each
		inputList.remove(big)
		listForBigNum.append(big)
		count =count+1
	#the above process get the ten larggest numbers in decending order

	#below process is to get position of larggest ten numbers in original list
	for each in listForBigNum:
		count1 = 0
		while count1<len(listOriginal):
			if each == listOriginal[count1] and len(listOfPosition) < 10:
			#do it this way to handle duplicate numbers in listForBigNum
				listOfPosition.append(count1)
			elif len(listOfPosition) ==10:
				return listOfPosition,listForBigNum,len(listOfPosition),len(listForBigNum)
			count1=count1 + 1

		#return inputList.index(big)#get the position of biggest num
print(larggestPosition(randomList))

with open('testDict.json') as f:
	data = json.load(f)
	tem = "car2"

	if tem in data:
		print(data[tem]["model"])
		print(data[tem]["brand"])
	for key,value in data.items():
		print(value["color"])
	templist = [] #测试最大数字
	for key,value in data.items():
		templist.append(value["count"])
	print(templist)
	#print(larggestPosition(templist))








