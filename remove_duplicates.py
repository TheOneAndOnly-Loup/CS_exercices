nums=[0,0,1,1,1,2,2,3,3,4]
nums.sort()
duplicates=0

for k in reversed(range(len(nums))):
    if nums[k] == nums[k-1]:
        nums.remove(nums[k])
        duplicates+=1
    else:
        continue


print(f"List with duplicates removed {nums}, number of duplicates: {duplicates}")