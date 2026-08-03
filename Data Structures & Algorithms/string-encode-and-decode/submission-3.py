class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += (f"{len(s)}#{s}")
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        ans = []
        length = 0
        i = 0

        while i in range(len(s)):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])

            i += 1 # jump to start of word
            ans.append(s[i: i + length])
            i += length

        return ans