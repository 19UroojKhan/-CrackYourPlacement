class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        top3_positive=heapq.nlargest(3,nums)
        top2_negative=heapq.nsmallest(2,nums)
        
        return max(top2_negative[0]*top2_negative[1]*top3_positive[0], 
                  top3_positive[0]*top3_positive[1]*top3_positive[2])
        