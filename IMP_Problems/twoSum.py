class Solution:
    def twoSum(self,nums,target):
        prev_map={}

        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in prev_map:
                return [prev_map[diff],i]
            else:
                prev_map[nums[i]]=i

s=Solution()
nums=[3,2,4,5,6,8]
res=s.twoSum(nums,7)
print(res)

#output: [0, 2]