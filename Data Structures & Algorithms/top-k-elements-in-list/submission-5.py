class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Accumulate counts O(n) time and O(n) space.
        counts = defaultdict(int)
        max_counts = 0
        for num in nums:
            counts[num] += 1
            max_counts = max(max_counts, counts[num])

        # Create an array of lists that contain the numbers which have i count.
        buckets = [[] for _ in range(max_counts + 1)]
        for num, count in counts.items():
            if not buckets[count]:
                buckets[count] = [num]
            else:
                buckets[count].append(num)
        
        # Iterate from right to left from the 
        # max element inserted and pop k items. O(n) Time
        k_frequent = []
        for i in range(max_counts, -1, -1):
            for j in range(len(buckets[i])):
                k_frequent.append(buckets[i][j])
                k -= 1

            if k == 0:
                break
        
        return k_frequent

# TC: O(n)
# MC: O(n)

        