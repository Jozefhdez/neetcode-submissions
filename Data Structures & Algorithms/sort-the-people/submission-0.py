class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = {}
        for i in range(len(names)):
            data[heights[i]] = names[i]
        
        sorted_heights = sorted(heights, reverse=True)
        return [data[h] for h in sorted_heights]

