from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(sorted_frequency[i][0])
        return ans



