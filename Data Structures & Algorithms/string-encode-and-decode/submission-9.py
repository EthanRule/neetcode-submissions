class Solution:

    def encode(self, strs: List[str]) -> str:
        # Rotate ascii forwards 1 character.
        encoded_strings = ""
        for item in strs:
            for ch in item:
                encoded_strings += chr(ord(ch) + 1)
            encoded_strings += ";"
        print(encoded_strings)
        return encoded_strings

# TC: O(n * m)
# MC: O(1) excluding result

    def decode(self, s: str) -> List[str]:
        # Rotate ascii backwards 1 character.
        decoded_strings = []
        current_string = ""
        for ch in s:
            if ch == ';':
                decoded_strings.append(current_string)
                current_string = ""
            else:
                current_string += chr(ord(ch) - 1)
        
        return decoded_strings
            

