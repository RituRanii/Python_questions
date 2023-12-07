str1 = input("Enter String in format:A1D3Y0")
alphabet = []
nums = []
for ch in str1:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        nums.append(ch)
final_list = sorted(alphabet)+sorted(nums)
output = ''.join(final_list)
print('Output:', output)