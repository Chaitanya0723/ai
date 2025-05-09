n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)


for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
