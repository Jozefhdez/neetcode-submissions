class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    
                    i += 1
                    j -= 1
                elif total < 0:
                    i += 1
                else:
                    j -= 1
        
        return ans