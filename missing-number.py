# Link: https://leetcode.com/problems/missing-number/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        arr  = [i for i in range(length)]
        return (set(arr) - set(nums)).pop()
