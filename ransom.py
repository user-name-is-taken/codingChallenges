class Solution:
    def canConstruct(self, cmp, base):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cmp = sorted(cmp)
        base = sorted(base)
        while len(cmp)>0 and len(base)>0 and base[0] <= cmp[0]:
            if cmp[0] == base[0]: del(cmp[0])
            del(base[0])
        if len(cmp) == 0: return True
        else: return False
        