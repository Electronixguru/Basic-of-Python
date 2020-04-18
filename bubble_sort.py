def sort(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp



nums = [10,8,5,12,9,3,2,1]
sort(nums)
print(nums)