class Solution:

    def encode(self, strs: List[str]) -> str:
        # Rotate ascii forwards 1 character.
        encoded_strings = ""
        for item in strs:
            encoded_strings += str(len(item)) + "#"
            for ch in item:
                encoded_strings += chr(ord(ch) + 1)
        print(encoded_strings)
        return encoded_strings

# TC: O(n * m)
# MC: O(1) excluding result

    def decode(self, s: str) -> List[str]:
        # Rotate ascii backwards 1 character.
        decoded_strings = []
        current_string = ""

        i = 0
        while i < len(s):
            word_length = ""
            while s[i] != "#":
                word_length += s[i]
                i += 1

            # print(word_length)
            i += 1
            # print(f"i: {i}, int(word_length) + 1: {i + int(word_length) + 1}")
            decoded_strings.append(s[i:i + int(word_length)])
            i += int(word_length)
            word_length_str = ""
            # print(f"new i: {i}")

        res = []
        for item in decoded_strings:
            decoded_item = ""
            for ch in item:
                decoded_item += chr(ord(ch) - 1)
            res.append(decoded_item)

        print(res)
        return res
            

