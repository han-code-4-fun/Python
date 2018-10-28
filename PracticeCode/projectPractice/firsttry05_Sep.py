import mitmproxy.http
from mitmproxy import ctx
import requests
import json
import sys
import subprocess
import os
import appiumForProject



class Counter:
    def __init__(self):
        self.num = 0


    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]



def getMETADATA(inputFile):
    command = ['ffprobe', '-show_format', inputFile]
    temp3 = subprocess.run(command, shell=True, capture_output=True).stdout.decode('utf-8')
    vidPos = temp3.find('vid:') + 4
    endPos = temp3.find('\r\n', vidPos)
    vidOutput = temp3[vidPos:endPos]
    return vidOutput



#convert the count into a partial name for future use
def covertDigg_count(inputNum):
    if inputNum<=49999:
        return "%"
    if inputNum>49999 and inputNum<100000:
        return "抖音5万赞+_"
    if inputNum>=100000 and inputNum<200000:
        return "抖音10万赞+_"
    if inputNum >= 200000 and inputNum < 300000:
        return "抖音20万赞+_"
    if inputNum >= 300000 and inputNum < 400000:
        return "抖音30万赞+_"
    if inputNum >= 400000 and inputNum < 500000:
        return "抖音40万赞+_"
    if inputNum >= 500000 and inputNum < 600000:
        return "抖音50万赞+_"
    if inputNum >= 600000 and inputNum < 700000:
        return "抖音60万赞+_"
    if inputNum >= 700000 and inputNum < 800000:
        return "抖音70万赞+_"
    if inputNum >= 800000 and inputNum < 900000:
        return "抖音80万赞+_"
    if inputNum >= 900000 and inputNum < 1000000:
        return "抖音90万赞+_"
    if inputNum >= 1000000 and inputNum < 1500000:
        return "抖音100万赞+_"
    if inputNum >= 1500000 and inputNum < 2000000:
        return "抖音150万赞+_"
    if inputNum >= 2000000 and inputNum < 3000000:
        return "抖音200万赞+_"
    if inputNum >= 3000000 and inputNum < 4000000:
        return "抖音300万赞+_"
    if inputNum >= 4000000 and inputNum < 5000000:
        return "抖音400万赞+_"
    if inputNum >= 5000000:
        return "抖音500万赞+_"


def removeIllegalCharForWinOS(inputString):
    illegal='\/:*?"<>|'
    temp = []
    for ele in inputString:
        if ele not in illegal:
            temp.append(ele)
    return ''.join(temp)

path = 'video/first/'

num = 0



#vidList = []

LengthListPreDownload = [] #this only used for avoid downloading duplicate file

number20 = 0


def saveALLFile(inputDict):
    with open("saveThemAll.json", mode="w", encoding='utf-8') as efg:
        json.dump(inputDict, efg, ensure_ascii=False, indent=2)

def saveToUpload(inputDict):
    with open("uploadedVideo.json", mode="w", encoding='utf-8') as tyu:
        json.dump(inputDict, tyu, ensure_ascii=False, indent=2)




def response(flow):
    global num,number20

    with open('uploadedVideo.json', mode='r', encoding='utf-8') as wer:
        uploaded = json.load(wer)

    with open('saveThemAll.json', mode='r', encoding='utf-8') as abc:
        allVideoJson = json.load(abc)  # file of all the videos ever downloaded

    target_type = 'video/mp4'

    json_target = 'com/aweme/v1/feed/'

    if json_target in flow.request.url:
        saveAllDict= dict()

        req = flow.response.content
        json_data = json.loads(req)
        cha = "cha_list"


        for currentVideo in json_data["aweme_list"]:

            vid = currentVideo["video"]["download_addr"]["uri"]
            likes= currentVideo["statistics"]["digg_count"]

            if vid in uploaded:
                #update digg_count(users likes)
                try:
                    uploaded[vid].upload({"点赞数":likes})
                    saveToUpload(uploaded)
                except Exception:
                    print('something wrong with digg_count data of current Json')
            else:
                videoid = currentVideo["aweme_id"]
                name = currentVideo["desc"]
                author_id = currentVideo["author_user_id"]
                author_nickname = currentVideo["author"]["nickname"]
                music_id = currentVideo["music"]["id"]
                saveAllDict[vid]={
                    "视频名": name,
                    "点赞数": likes,
                    "视频id": videoid,
                    "作者id": author_id,
                    "作者名": author_nickname,
                    "音乐id": music_id,
                    "下载": 0

                }
               
                if cha in currentVideo: #which means this video joins a #topic
                    cid = currentVideo["cha_list"][0]["cid"]
                    cha_name = currentVideo["cha_list"][0]["cha_name"]
                    user_count = currentVideo["cha_list"][0]["user_count"]
                    saveAllDict[vid].update({
                        "话题id": cid,
                        "话题名": cha_name,
                        "话题用户数": user_count
                    
                    })
                  
                allVideoJson.update(saveAllDict)
                saveALLFile(allVideoJson)



    # above process is to save the list of videos into a custom lists in local folder
    #below part is to download videos,
    else:

        #for ele in target_urls:
           # if flow.request.url.startswith(ele):

        if flow.response.headers.get('Content-Type') == target_type: #if it's a mp4 file
            flow.response.stream = True
            contentLength = flow.response.headers.get('Content-Length')
                 
           
           # if vid not in allVideoJson:

            if contentLength in LengthListPreDownload:
                print('duplicate file     duplicate file     duplicate file     '
                        'duplicate file     duplicate file     duplicate file     ')
                print(len(LengthListPreDownload))
            else:

                #1.download   and name in num
                #2.check if vid is in the dict  allVideoJson, if not, delete
                #     if yes,  use vid to check if it's been downloaded already
                # if downloaded, remove file named num, 
                # if not downloaded before,  use it's vid to get file name
                #    rename the file, update it's download status
                #     add it's content length into LengthListPreDownload
                #3. scroll

               
                print("pass length check     pass length check     pass length check    pass length check \
                    pass length check     pass length check     pass length check    pass length check ")

                res = requests.get(flow.request.url, stream=True)

                filename = path + str(num) +'.mp4'

                with open(filename, 'wb') as ffff:
                    ffff.write(res.content)
                    ffff.flush()
                    num = num + 1
                
                thisvid = getMETADATA(filename)

                if thisvid in uploaded:#already downloaded and uploaded
                    os.remove(filename)

                else:

                    if thisvid in allVideoJson:
                        
                        if allVideoJson[thisvid]["下载"] > 0: #this file have been downloaded before
                            os.remove(filename)
                            print('downloaded before  before  before  before  before  before  before  before \
                            before  before  before  before  before  before  before  before  before  before ')
                        else:#this file hasn't been downloaded before
                            name = removeIllegalCharForWinOS(allVideoJson[thisvid]["视频名"])
                            videoid = allVideoJson[thisvid]["视频id"]
                            likes = allVideoJson[thisvid]["点赞数"]
                            newfilename = path + covertDigg_count(likes) + name + videoid + '.mp4'
                            os.rename(filename,newfilename)
                            allVideoJson[thisvid]["下载"] = 1
                            saveALLFile(allVideoJson)
                            LengthListPreDownload.insert(0, contentLength)
                            if likes > 1000000-1:
                                number20 = number20 + 1
                                if number20 >= 20:
                                    sys.exit()
                            appiumForProject.action.scroll()

                    else:
                        os.remove(filename)
                        #write an error report
                        with open('errorStrangeFile.txt',mode='a+',encoding='utf-8') as errStra:
                            errStra.write('vid: \r\n')
                            errStra.write('    ')
                            errStra.write(thisvid)
                            errStra.write('\r\n')



                
