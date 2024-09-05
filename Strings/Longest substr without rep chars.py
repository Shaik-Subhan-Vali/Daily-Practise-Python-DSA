def dup(st):
    if len(st) == len(set(st)):
        return True
    
s="nmbvcfynnckiarnnekdubabcksus"
mlen=0
for i in range(0, len(s)):
    for j in range(i+1, len(s)):
        s1 = s[i:j]
        if dup(s1):
            if len(s1) > mlen :
                mlen = len(s1)
print(mlen)

# Using a Sliding Window with Two Pointers

left=0
maxlen=0

dups = set()
for x in range(len(s)):
    while s[x] in dups:
        dups.remove(s[x])
        left +=1

    dups.add(s[x]) 
    maxlen = max(maxlen, x - left + 1)
print(maxlen)