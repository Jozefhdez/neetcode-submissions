class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in s:
            if i - 1 not in s:
                num = i
                l = 1
                while num + 1 in s:
                    l += 1
                    num += 1
                longest = max(l, longest)
        
        return longest