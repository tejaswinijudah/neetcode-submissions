class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        seen = set()
        maxlen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])    
            maxlen = max(maxlen, right - left +1)
        return maxlen
# key learnings: for sets - no duplicates allowed,
# seen.add() is right, not seen.append() - thats for list

