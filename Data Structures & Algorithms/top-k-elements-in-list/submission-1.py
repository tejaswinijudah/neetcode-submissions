class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num]= 1+ count.get(num,0)
# getting the freq of numbers in the list. mapping it as number -> freq
        arr =[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
# getting the key(number) and value(freq) of the dictionary and putting them in reverse order in the array i.e. [freq, number]
# because when we do arr.sort() it sorts by seeing the first element, in this case - cnt, freq.
# because we want the highest freq numbers in the last to pop it easily
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
# creating a res array to store the result. using a while loop to pop elements from arr and put it in res. 
# arr.pop() gives [freq,number]
# arr.pop()[1] gives the element in index 1 which is the number, freq is index 0
# and appending that number (highest frequency number) to the result. and repeating this for k times until we get the top K frequent elements in the given list, voila!
# while len(res) < k:      uf k=2
# initially len(res) is 0, loop runs once
# then len(res) = 1, loop runs once more, second time, now the res contains k elements (2) and the loop has to stop, that's why is <k and not <= k. if it is <= k then loop will run for a third time making res contain 3 elements which we dont want.
# takeaway ~ while smtg < k:  the loop runs k times,
# while smtg <= k the loop runs k+1 times. 
# time complexity is O(nlogn) - better method is bucket sort O(n)
        