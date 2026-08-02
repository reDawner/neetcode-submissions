class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        maps = {}

        for i in range(n):
            maps[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in maps and maps[complement] != i:
                return [i, maps[complement]]