a = '手机???的?"<>|撒//撒/\大\家:搜*啊\k/k:k*k?k"k<k>k|E'
b='\/:*?"<>|'
c = []
z = 0
while z < len(a):
    if a[z] in b:
        z = z + 1
    else:
        c.append(a[z])
        z = z +1
print(c)
d = ''.join(c)
print(d)
print(len(d))
print(type(d))

print(' ')
def removeIllegalCharForWinOS(inputString):
	illegal='\/:*?"<>|'
	temp = []
	for ele in inputString:
		if ele not in illegal:
			temp.append(ele)
	return ''.join(temp)

print(removeIllegalCharForWinOS(a))
print(type(removeIllegalCharForWinOS(a)))
print(len(removeIllegalCharForWinOS(a)))