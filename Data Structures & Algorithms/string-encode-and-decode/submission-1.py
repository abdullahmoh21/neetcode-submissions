class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + '#'
            string += s
        return string


    def decode(self, s: str) -> List[str]:
        strings = []
        len_start = 0
        len_end = 0
        i = 0
        while i < len(s):
            len_start = i
            len_end = i
            while s[i] != '#':
                len_end += 1
                i+=1 
            length = int(s[len_start:len_end])
            string_start = len_end + 1
            strings.append(s[string_start:string_start + length])
            i = string_start + length 
        return strings









