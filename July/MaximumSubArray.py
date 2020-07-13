class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        CurSum = MaxSum = nums[0]
        for num in nums[1:]:
            CurSum = max(num, CurSum+num)
            MaxSum = max(MaxSum, CurSum)
        return MaxSum