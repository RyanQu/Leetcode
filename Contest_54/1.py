#Input: [1,2,2,3,1,4,2]
#Output: 6

nums = [1,2,2,3,1,4,2]
def findShortestSubArray(nums):
    inverse_nums = nums[::-1]
    unit=[]
    total=[]
    lenth=[]
    #[number,times,first,last]
    temp=len(nums)

    for i in range(temp):
        if nums[i] not in unit:
            unit.append(nums[i])
            times = nums.count(nums[i])
            first = nums.index(nums[i])
            last = len(nums)-inverse_nums.index(nums[i])
            total.append(times)
            lenth.append(last-first)

    print unit
    print total
    print lenth
    flag = max(total)

    for j in range(len(total)):
        if total[j]==flag:
            temp=min(temp,lenth[j])
    return temp

print findShortestSubArray(nums)