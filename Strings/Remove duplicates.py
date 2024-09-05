s="eichokrjusownaocinaskoidams"
s1=""
uniq =set()
for x in s:
    if x not in s1:
        s1 += x
print(s1) 
for x in s:
    uniq.add(x)
print("".join(uniq))
