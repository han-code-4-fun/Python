a = ['1809300', '2211828', '4220301', '1106980', '1135000', '1261847', '1778313', '163089', '1112196', '764821', '233347', '1613331', '1080115', '2346823', '2388814', '507145', '1998337']

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

check(a)

print(len(a))
