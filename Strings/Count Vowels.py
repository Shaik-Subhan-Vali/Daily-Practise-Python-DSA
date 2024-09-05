from collections import Counter

s="aennfjcoejoijkaknNACEIOSMANEIOE"
vow="aeiou"
c=0
for x in s.lower():
    if x in vow:
        c +=1
print(c) 
print(sum(1 for x in s.lower() if x in vow))    
