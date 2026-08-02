class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num in freq:
            frequency = freq[num]
            buckets[frequency].append(num)

        result = []
        for num in range(len(buckets) - 1, 0, -1):
            for i in buckets[num]:
                result.append(i)
                if len(result) == k:
                    return result