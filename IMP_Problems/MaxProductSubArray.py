class Solution:
    def maxProdSubarray(self,nums):
        res= nums[0] #Initialising max product to first element
        curr_max = 1
        curr_min = 1

        for n in nums:
            tmp = n*curr_max
            curr_max = max(n*curr_max , n*curr_min , n)
            curr_min = min(tmp , n*curr_min , n)
            #print(curr_max , curr_min)

            res = max(res,curr_max)
            #print(res)

        return res


nums = [2,3,-2,4]
res = Solution().maxProdSubarray(nums)
print(res)


#Result = 6
#Time Complexity = O(n)



