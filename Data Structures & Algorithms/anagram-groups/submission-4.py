class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        # O(n * mlogm)
        for item in strs:
            sorted_item = ''.join(sorted(item))
            groups[sorted_item].append(item)
        
        # Loop over keys in O(n) and append to final list
        return list(groups.values())

# Expected Time Complexity: O(n * mlogm) where n is the count of strings, and m is the
# maximum length of a string.

# Expected Space Complexity: O(n * m) where n is the count of strings in strs, and 
# m is the maximum lenght of a string in strs.
