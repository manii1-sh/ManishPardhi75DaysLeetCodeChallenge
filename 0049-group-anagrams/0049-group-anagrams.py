class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        groups = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            groups[sorted_word].append(word)

        return list(groups.values())