class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res=0
        maxleft, maxright =height[l], height[r]
        if not height:
            return 0
        while l<r:
            if maxleft<maxright:
                l+=1
                maxleft = max(height[l],maxleft)
                res += maxleft-height[l]
                        
            else:
                r-=1
                maxright = max(height[r],maxright)
                res += maxright-height[r]  
        return res   