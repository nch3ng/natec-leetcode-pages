from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_hash = OrderedDict()
        index_hash = OrderedDict()

        for i,c in enumerate(s):
          if c in count_hash:
            count_hash[c] += 1
          else:
            index_hash[c] = i
            count_hash[c] = 1

        while count_hash:
          (key, count) = count_hash.popitem(last=False)
          if count == 1:
            return index_hash[key]

        return -1