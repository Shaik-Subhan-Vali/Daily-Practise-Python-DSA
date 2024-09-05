arr=[13,32,43,67,8,32,5,31,7,2,32]
n =len(arr)
k =4
window_sum=sum(arr[:k])
min_sum=window_sum
for i in range(k,n):
    window_sum += arr[i] - arr[i-k]
    min_sum = min(window_sum, min_sum)
print(min_sum)
