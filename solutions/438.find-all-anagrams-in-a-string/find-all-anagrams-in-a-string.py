# all lower case
# possible the same alphabet in p or s
# p is empty
# p is longer than s
# max

class Solution:
    def findAnagrams(self, s, p):
        ans = []
        if s == None or p == None:
            return ans

        len_s, len_p = len(s), len(p)

        if len_p > len_s:
            return ans

        hash_p = dict()

        for c in p:
            if c in hash_p:
                hash_p[c] += 1
            else:
                hash_p[c] = 1        
        
        window_hash = dict()
        for i in range(len_s):
            if i > len_p - 1:
                # print(window_hash)
                if window_hash[s[i-len_p]] == 1:
                    del window_hash[s[i-len_p]]
                else:
                    window_hash[s[i-len_p]] -= 1

            # print(window_hash)
            c = s[i]
            if c in window_hash:
                window_hash[c] += 1
            else:
                window_hash[c] = 1

        # for i in range(len_s - len_p + 1):
        #     window_hash = self.populateHash(s[i:i+len_p])

            if window_hash == hash_p:
                ans.append(i-len_p+1)

        return ans