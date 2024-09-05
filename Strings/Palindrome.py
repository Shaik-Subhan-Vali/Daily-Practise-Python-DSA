s="htth"
s1=""
s2=""
for x in s:
    s1 = x + s1    
if s1==s:
    print("Palindrome")
else:
    print("Not Palindrome")        

s2="".join(reversed(s))
if s2==s:
    print("Palindrome")
else:
    print("Not Palindrome")    

#two pointers concept

status= True
left=0
right=len(s)-1
while left <right:
    if s[left]!=s[right]:
        status = False
        break
    left+=1
    right-=1
if status==True:
    print("Palindrome")
else:
    print("Not Palindrome")
