class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix multiplication arr
        # postfix multiplication arr
        # for i multiply the prefix[i] * postfix[i]

        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        print(prefix)
        print(postfix)
        
        return [prefix[i] * postfix[i] for i in range(n)]