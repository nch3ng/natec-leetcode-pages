class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        list = []

        for c in S:
          list.append(c)
        for jc in J:
          n = len(list)
          i = 0
          while i < n:
            c = list[i]
            if jc == c:
              ans += 1
              list.pop(i)
              n -= 1
            else:
              i += 1
              
        return ans
