import json

#this is for testing python json I/O

with open("testDict.json") as f:
	jsonData = json.load(f)
	#jsonData["car4"]["COLOR"] = "test"


def saveChanges():
	with open("testDict.json","w") as s:
		json.dump(jsonData, s, indent=2)


print(type(jsonData))


var = "car1"
if var in jsonData:
	print("yes")
else:
	print("no")

var2= "brand"
if var2 in jsonData:
	print("yes")
else:
	print("no")

var3='car4'
var3_1='diamond'

if var3 in jsonData:
	jsonData["car4"]["color"] = var3_1
	#saveChanges()
	print(jsonData["car2"]["model"])
the = {"test":"drive"}
jsonData["car4"].update(the)

chaDict = {
	                        "话题id": "cha_list",
	                        "话题名称": "cha_list",
	                        "话题人数": "user_count"
	                        }
jsonData["car4"].update(chaDict)

tempDict = dict()

tempDict["aweme_id"] = {
	"视频名称":"desc",
	"点赞数": "statistics",
	"作者id": "author_user_id",
	"作者名称": "nickname",
	"音乐id": "music"
}

chaDict = {
	"话题人数": {"user_count":"another"},
	"话题id": "cid",
	"话题名称":"cha_name"

}
tempDict["aweme_id"].update(chaDict)
tempDict["id2"]= "id2of the list"

jsonData.update(tempDict)

print(json.dumps(jsonData, ensure_ascii=False, indent=2))
print(json.dumps(tempDict, ensure_ascii=False, indent=2))
for ele in jsonData:
	print(ele)
