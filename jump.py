class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        jumps = 0           
        curr_end = 0        
        farthest = 0        

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1              
                curr_end = farthest     
        return jumps