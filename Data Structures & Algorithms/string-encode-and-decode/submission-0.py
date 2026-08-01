class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ",".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return s.split(',')


