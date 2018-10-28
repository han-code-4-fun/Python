import os

a='1.txt'

b='12.txt'



try:
    os.rename(b,a)
except FileExistsError:
    os.rename(b,"1"+a)