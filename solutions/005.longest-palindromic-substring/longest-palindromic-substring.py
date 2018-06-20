class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=0
        dp = [[False] * len(s) for _ in range(len(s))]
      #  return dp
        for i in reversed(range(len(s))):
            for j in range(i,len(s)):
                if  s[i]==s[j] and (j-i<3 or dp[i+1][j-1]==True):  
                    dp[i][j]=True

                if dp[i][j]==True and length<=j-i+1: 
                    length=j-i+1
                    ans=s[i:j+1]    
        return ans  