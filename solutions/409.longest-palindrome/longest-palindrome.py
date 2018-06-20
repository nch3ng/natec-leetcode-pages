# empty return 0
# 1 char return 1
# only 26 alphabits with both lower and upper case
# no special chars

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0 
        len_s = len(s)
      
        if len_s in [0,1]:
            return len_s
        
        hash = dict()
        
        for i in range(len_s):
            if s[i] in hash:
                hash[s[i]] += 1
            else:
                hash[s[i]] = 1
        
        single_exist = 0
        
        for char in hash:
            if hash[char] % 2 == 1:
                single_exist = 1
                hash[char] -= 1
            
        for char in hash:
            ans += hash[char]
            
        ans += single_exist
            

        return ans