# Link: https://leetcode.com/problems/fruits-into-baskets-ii/
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for i in range(len(fruits)):
            for j in range (len(baskets)):
                if fruits[i] <= baskets[j]:
                    fruits[i] = 0
                    baskets[j] = 0
                    break
        print(fruits)
        return len(fruits) - fruits.count(0)
    
def main():
    s = Solution()
    print(s.numOfUnplacedFruits([4,2,5], [3,5,4]))

if __name__ == '__main__':
    main()