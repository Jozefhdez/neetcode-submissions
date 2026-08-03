class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            ans[''.join(sorted(s))].append(s)
        
        return [i for i in ans.values()]