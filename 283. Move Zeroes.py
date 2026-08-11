
class Solution:
    def moveZeroes(self, nums: list[int]):

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1

        print(nums)

        
        


if __name__ == "__main__":
    obj = Solution()
    obj.moveZeroes([0, 1, 0, 3, 12,])  # [1, 3, 12, 0, 0]






    