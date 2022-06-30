def twoSum(nums, target):
    index_map = {}
    for i in range(len(nums)):
        print(index_map)
        num = nums[i]
        pair = target - num

        if pair in index_map:
            return [index_map[pair], i]
        index_map[num] = i
    return None

#nums=[3,2,4,5,6,8]
nums=[5,9,3,7,2,8]

res=twoSum(nums,16)
print(res)