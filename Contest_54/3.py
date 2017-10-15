"""
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""

def canPartitionKSubsets(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    s=sum(nums)
    if s%k!=0:
        return False

    flag=s/k
    temp=[]
    for i in range(len(nums)):
        if 