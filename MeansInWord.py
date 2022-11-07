from PyDictionary import PyDictionary
dic = PyDictionary()
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
			try:
				try:
					hhh=dic.meaning(p,disable_errors=True)
				except:
					hhh=None
				for lol in hhh:
					for g in range(len(hhh[lol])):
						print(f"\t{g+1}.",p,f' as a {lol} :\t',hhh[lol][g],"\n")
			except:
				print("\t",p," : Unknown meaning")

print('Found',len(final_cd),"words")