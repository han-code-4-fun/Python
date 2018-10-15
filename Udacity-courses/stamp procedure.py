# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(a):
    # Your code here
    output1 = 0
    output2 = 0
    output3 = 0
    while (a >=5):
        a= a-5
        output1 = output1 +1
    while (a>=2):
        a= a -2
        output2 = output2 +1
    while (a==1):
        a = a-1
        output3 = 1
   # print output1
    output1= str(output1)
    output2= str(output2)
    output3= str(output3)
  #  if(a == 0):
    return '(' + output1 +','+ output2+','+output3+')'
   
        

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
