arr=[1,2,4,6,3,2,5,7,3,3]
k=3
n= len(arr)
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k,n):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(window_sum, max_sum)
print(max_sum)