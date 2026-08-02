class Solution:

    def encode(self, strs: List[str]) -> str:
        size = []
        for i in strs:
            size.append(str(len(i)))
        string = ",".join(size)
        newstr = string + "#"
        anotherstr = ''.join(strs)
        newnewstr = newstr + anotherstr
        return newnewstr

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        astr, bstr = s.split('#', 1)

        if astr == "":     #if atr is null, then next step (convertion to int) wont work
            return []

        string = [int(x) for x in astr.split(',')]

        res = []
        i = 0
        for st in string:
            res.append(bstr[i:i + st])
            i += st
        
        return res
