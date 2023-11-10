class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            d1 = {}
            for str in strs:
                sorted_str = ''.join(sorted(str))
                d1[sorted_str] = d1.get(sorted_str, []) + [str]
            return d1.values()
            
        