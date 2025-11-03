class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ph = 0
        for seeker in range(len(nums)):
            # nums[seeker] is false when it is zero
            if nums[seeker]:
                #swap
                nums[ph],nums[seeker] = nums[seeker] ,nums[ph]
                ph+=1

