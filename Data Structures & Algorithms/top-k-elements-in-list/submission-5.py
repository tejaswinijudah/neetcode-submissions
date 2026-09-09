class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num]= 1+ count.get(num,0)
# getting the freq of numbers in the list. mapping it as number -> freq
        freq = [[] for i in range(len(nums)+1)]
        for num,cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num  in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
## freq is an array of buckets where the INDEX represents the frequency.
# A number can appear at most len(nums) times, so we need buckets from 0 to len(nums).
#
# Example: len(nums) = 6
# range(len(nums) + 1) gives indexes 0 to 6
#freq = [[] for i in range(len(nums)+1)]
# freq = [
#     [],  # frequency 0
#     [],  # frequency 1
#     [],  # frequency 2
#     [],  # frequency 3
#     [],  # frequency 4
#     [],  # frequency 5
#     []   # frequency 6
# ]
#creating 7buckects, because we need index till len(nums) which is 6, so we need freq index till 6, automatically freq index starts from 0 to ... sor len(freq) is 0 to 6 which is = 7, so we obviously need len(nums) +1 in the for loop
# If nums = [1,1,1,2,2,3], then:
# count = {1: 3, 2: 2, 3: 1}
#
# Put each number into the bucket corresponding to its frequency:
# index of freq = count.value which is the frequency of the number
# freq[cnt].append(num)
#
# So:
# freq[3] = [1]  -> 1 appeared 3 times
# freq[2] = [2]  -> 2 appeared 2 times
# freq[1] = [3]  -> 3 appeared 1 time
#
# Then traverse the buckets backwards, from highest frequency to lowest:
# range(len(freq)-1, 0, -1)
#
# This gives: 6, 5, 4, 3, 2, 1
#
# For each bucket, add its numbers to res.
# Stop and return as soon as we have k numbers.
#
# Example with k = 2:
# freq[3] -> [1] -> res = [1]
# freq[2] -> [2] -> res = [1, 2]
# len(res) == k, so return [1, 2]
#
# KEY IDEA:
# Frequency becomes the array index (bucket).
# This avoids sorting and gives O(n) time complexity.