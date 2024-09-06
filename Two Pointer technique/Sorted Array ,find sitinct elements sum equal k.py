#Given a sorted array of integers arr and a target sum k, find if there are two distinct elements in the array that sum up to k
arr=[1,3,4,5,6,7,9]
n=len(arr)
k=9
for i in range(n):
    for j in range(i+1, n-1):
        if arr[i] +arr[j] ==k:
            print(arr[i], arr[j])

#Two pointer approach
#sorted array kabbati increasing order
i =0
j =n-1
while i<j:
    sum = arr[i] + arr[j]
    if sum == k:
        print(arr[i], arr[j])
        break
    elif sum < k:    
        i +=1
    else:
        j -=1



