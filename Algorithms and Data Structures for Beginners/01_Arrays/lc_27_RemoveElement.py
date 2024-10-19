# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        pointer = 0
        counter = 0 

        i = 0 
        while i < len(nums):
            if nums[i] == val:
                pass
            else:
                nums[pointer] = nums[i]
                counter += 1
                pointer += 1
            i += 1
        
        return counter


        