class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = 0
        if len(trust) > 0:
            judge = trust[0][1]

        for pair in trust:
            if pair[1] != judge:
                return -1
            elif pair[0] == judge:
                return -1

        return judge