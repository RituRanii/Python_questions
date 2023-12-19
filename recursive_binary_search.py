def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid], target)
            
def verify(index):
        print("Target found :", result)

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)