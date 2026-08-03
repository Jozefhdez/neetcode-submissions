class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count how many times they appear in the List
        # sort them from most to least frequent
        # pop k

        heap_list = [(-times, element) for element, times in Counter(nums).items()]
        heapq.heapify(heap_list)
        return [heapq.heappop(heap_list)[1] for _ in range(k)]