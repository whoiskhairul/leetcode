# link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        l = len(nums)
        arr = [i for i in range(1, l + 1)]
        return list(set(arr) - set(nums))