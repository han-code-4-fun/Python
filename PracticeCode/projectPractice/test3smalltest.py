import random,json
#this is to test the immutability of list in python
list1=[291, 127, 691, 35, 952, 267, 267, 26, 868,
       580, 415, 105, 69, 65, 159, 813, 226, 262,
       636, 832, 427, 15, 304, 275, 497, 252, 541,
       243, 986, 602, 184, 696, 245, 366, 938, 265,
       905, 965, 823, 587, 266, 445, 298, 737, 874,
       949, 464, 794, 134, 775, 175, 110, 639, 730,
       642, 247, 523, 627, 21, 608, 997, 54, 164, 676,
       883, 567, 246, 630, 993, 113, 873, 583, 744,
       725, 566, 91, 337, 517, 498, 269, 780, 47, 984,
       652, 206, 685, 83, 456, 334, 964, 970, 899, 425,
       54, 417, 800, 164, 714, 48, 219, 759, 946, 627,
       13, 827, 500, 72, 902, 609, 295, 492, 628, 252,
       969, 815, 720, 712, 350, 658, 556, 139, 889,
       861, 101, 787, 61, 42, 160, 339, 733, 886, 258,
       126, 58, 5, 18, 86, 953, 788, 24, 415, 466, 313,
       407, 797, 429, 819, 61, 394, 775, 835, 8, 709,
       105, 598, 348, 755, 823, 985, 401]


#for x in range(160):
#	list1.append(random.randint(1,1000))

list2=[]

def removeDuplicate(inputList):
    temList = inputList.copy()
    for ele in inputList:
        count = 0
        for eee in temList:
            if ele == eee:
                count = count + 1
            if count == 2:
                temList.remove(eee)
    return temList



def check(input):
    for each in input:
        count =0
        for ele in input:
            if each ==ele:
                count = count + 1
                if count >1:
                    print('yes duplicate')
                    return
    print('no duplicate')
    return

list2 = removeDuplicate(list1)
check(list1)
check(list2)

print(list2)

list2= [291, 127, 691, 35, 952, 267, 26, 580, 65,
        813, 262, 832, 15, 275, 243, 602, 696, 366,
        265, 965, 587, 445, 737, 949, 794, 110, 730,
        247, 608, 676, 567, 630, 113, 583, 725, 91, 517,
        269, 47, 652, 685, 456, 964, 899, 54, 800,
        219, 627, 500, 295, 252, 720, 556, 101, 160,
        258, 18, 24, 407, 61, 8]

print(len(list2))




def positionOfNOBiggerThan400(inputList):
    tem = []
    for ele in inputList:
        if ele > 400:
            tem.append(list2.index(ele))
    return tem

print(positionOfNOBiggerThan400(list2))
#result [2, 4, 7, 9, 11, 15, 16, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 33, 34, 36, 39, 40, 41, 42, 43, 45, 47, 48, 51, 52, 58]







































