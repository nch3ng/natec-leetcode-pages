from collections import deque
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        
        all_combo = ['']
        for d in digits:
            current_combo = []
            for c in mapping[d]:
                for prev in all_combo:
                    current_combo.append(prev+c)
                    # print(current_combo)
                
            all_combo = current_combo
        
        return all_combo
            