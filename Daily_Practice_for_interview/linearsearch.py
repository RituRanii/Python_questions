def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return f" the value of {target} is in the index position {i}"
    return -1
numbers = [1,4,6,9,10,13]
result = linear_search(numbers,9)
print(result)