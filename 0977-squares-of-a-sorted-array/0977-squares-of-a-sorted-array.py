class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [0]*len(nums)
        for i in range (len(nums)):
            new_nums[i]=nums[i]**2
        new_nums.sort()
        
        return new_nums
        
        
        