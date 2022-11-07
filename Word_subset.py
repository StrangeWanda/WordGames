f=open("theWL.txt",'r')
g=open("words.txt",'r')
lol = (f.read().split("\n")) + (g.read().split("\n"))
f.close()
g.close()

word = input("Enter the string:\t").lower()
final_cd=[]

for words in lol:
		wymm=1
		wordi=list(word)
		for lett in words:
			if lett in wordi:
				wordi.remove(lett)
				continue
			else:
				wymm=0
				break
		if wymm==1:
			final_cd.append(words)
			

for k in range(1,len(word)+1):
	print('_'*20)
	print(f'{k} letter words')
	print('-'*20)
	for p in set(final_cd):
		if len(p) == k:
			print("\t",p)

print('Found',len(final_cd),"words")
from msvcrt import getch as w
w()
