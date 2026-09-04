class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap , self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

# mistakes i made- syntax error, forgot to use self.k, used k instead - mistake 1
# instead of heapq.heap blah blah i used normal python way like self.minheap.append(val) - wrong