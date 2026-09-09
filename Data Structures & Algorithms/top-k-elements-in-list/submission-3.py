class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num]= 1+ count.get(num,0)
# getting the freq of numbers in the list. mapping it as number -> freq
        heap = []
        heapq.heapify(heap)
        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            # tuple is created here, list could also be created
            if len(heap) >k:
                heapq.heappop(heap)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

# 

#* **Both lists `[]` and tuples `()` work** with `.sort()` and `heapq` as long as their elements are comparable.
#* `[]` = **list** (mutable), `()` = **tuple** (immutable).
#* The sorting solution **could also use tuples**; using a list isn't necessary.
#* In the heap solution, `(freq, num)` is commonly used because it represents a fixed **`(priority, value)` pair**.
#* For heaps, think:

#```python
#(freq, num)
#   ↓    ↓
# priority  value
#```

#* `heapq` does **not** require tuples.
#* Both work with indexing:

#```python
#[3, 1][1]  # 1
#(3, 1)[1]  # 1
#```

#**Key DSA pattern:**
#`heapq.heappush(heap, (priority, value))` → **heap is ordered primarily by `priority`.**
   
