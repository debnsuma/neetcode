# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0 
        arr_len = len(nums)

        i = 0
        last_seen = nums[i]
        while i < arr_len:
            if nums[i] == last_seen:
                pass
            else:
                pointer += 1
                nums[pointer] = nums[i]
                last_seen = nums[i]
            i += 1
        
        return pointer+1
        