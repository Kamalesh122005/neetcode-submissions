class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        width=0
        maxi=float('-inf')
        while l<r:
            height=min(heights[l],heights[r])
            width=r-l
            area=height*width
            maxi=max(maxi,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxi




        