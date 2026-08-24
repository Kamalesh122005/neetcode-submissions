class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        ans=0
        for i in range(len(heights)+1):
            if i==len(heights):
                curr=0
            else:
                curr=heights[i]
            while stack and heights[stack[-1]] >= curr:
                h=heights[stack.pop()]
                if stack:
                    left=stack[-1]
                else:
                    left=-1
                width=i-left-1
                ans=max(ans,h*width)
            if i<len(heights):
                stack.append(i)
        return ans
        