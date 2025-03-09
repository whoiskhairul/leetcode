# link: https://leetcode.com/problems/counting-bits/
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(str(bin(i)).count('1'))
        return res


def main():
    s = Solution()
    print(s.countBits(5))

if __name__ == '__main__':
    main()