class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            cur_max = 0
            max_i = 0
            for i in range(len(gifts)):
                if gifts[i] > cur_max:
                    cur_max = gifts[i]
                    max_i = i
            print(gifts[max_i])
            gifts[max_i] = floor(sqrt(gifts[max_i]))

        return sum(gifts)
