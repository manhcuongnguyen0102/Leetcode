from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = defaultdict(list)
        for s in strs:
            letter = [0]*26
            for char in s:
                index = ord(char) - ord('a')
                letter[index]+=1
            encode = tuple(letter)
            anagrams_map[encode].append(s)
        return list(anagrams_map.values())
        
