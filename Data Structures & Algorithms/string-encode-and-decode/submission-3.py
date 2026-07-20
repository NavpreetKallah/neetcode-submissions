class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += f"{len(string)}-{string}"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        strLength = ""
        length = 0
        word = ""
        print(s)
        for letter in s:
            if letter == "-":
                length = int(strLength)
                strLength = ""
                output.append(word)
                word = ""
            elif length == 0:
                strLength += letter
            else:
                length -= 1
                word += letter
        output.append(word)
        output.pop(0)
        return output

