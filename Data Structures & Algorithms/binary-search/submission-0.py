class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            #efficiently find the midpoint
            mid = (left + right) //2

            if nums[mid] == target:
                return mid #if target is found, then it shall return its index

            elif nums[mid] < target:
                left = mid + 1 #target is in the right half
            else:
                right = mid - 1 #target is in the left half

        return -1 