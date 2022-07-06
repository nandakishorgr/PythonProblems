#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution:
    def maxSubarray(self,nums):
        maximum_sum_so_far = nums[0]    #Initialising max sum to first element
        currSum = 0

        for n in nums:
            if currSum < 0:             #If current sum is negetive value then re-assigning currSum to zero
                currSum = 0
            currSum = currSum + n

            maximum_sum_so_far = max(maximum_sum_so_far,currSum)

        return maximum_sum_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-2,4,1,-3]
#nums1=[-2,-1]
result=Solution().maxSubarray(nums)
print(result)



#Result=6
#Result1=-1 ====> for [-2,-1]  the max sub array is : [-1] so max sum is -1

#TimeComplexity = O(n)



