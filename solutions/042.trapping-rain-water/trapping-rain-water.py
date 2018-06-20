# if only one or two bar return 0
# only positive integer
# max? assume 1000 bar

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        ans = 0
        
        len_h = len(height)
        
        if len_h in [0,1]:
            return ans
        
        max_left = [0 for i in range(len_h)]
        max_right = [0 for i in range(len_h)]
        
        # find the max_left for each bar from 1 - len_h-2, the max_left of first bar is 0
        max_left[0] = height[0]
        for i in range(1,len_h-1):
            if height[i] > max_left[i-1]:
                max_left[i] = height[i]
            else:
                max_left[i] = max_left[i-1]

                
        # find max_right for each bar from len_h - 2 to 1, the max_right of the last bar is 0
        max_right[len_h-1] = height[len_h-1]
        for i in range(len_h-2, 0, -1):
            if height[i] > max_right[i+1]:
                max_right[i] = height[i]
            else:
                max_right[i] = max_right[i+1]
        for i in range(i,len_h-1):
            ans += min(max_left[i], max_right[i]) - height[i]
            
        return ans
        
        
# height =   [0,1,0,2,0,1,2,3,2,1,0,2,0,1]
# max_left = [0,1,1,2,2,2,2,3,3,3,3,3,3,0]
# max_right =[0,3,3,3,3,3,3,3,2,2,2,2,1,0]

        