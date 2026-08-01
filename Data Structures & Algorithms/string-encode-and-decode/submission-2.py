class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ",".join(strs)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = s.split(',')
        if decoded_string == [""]:
            decoded_string = []
        print(decoded_string)
        return decoded_string


