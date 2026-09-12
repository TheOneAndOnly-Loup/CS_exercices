nums=[1,1]
nums.sort()
duplicates=0
for k in reversed(range(len(nums))):
    if len(nums)==1:
       break 
    if nums[k] == nums[k-1]:
        nums.remove(nums[k])
        duplicates+=1
    else:
        continue


print(f"List with duplicates removed: {nums}, number of duplicates: {duplicates}")
print("test")