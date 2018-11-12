import heapq
class Solution:
    def canConstruct(self, cmp, base):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cmp = list(cmp)
        base = list(base)
        heapq.heapify(cmp)
        heapq.heapify(base)
        while len(cmp)>0 and len(base)>0 and base[0] <= cmp[0]:
            if cmp[0] == base[0]: heapq.heappop(cmp)
            heapq.heappop(base)
        if len(cmp) == 0: return True
        else: return False
        