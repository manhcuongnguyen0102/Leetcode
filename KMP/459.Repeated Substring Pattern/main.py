class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        def lps(s):
            do_dai = 0
            i = 1
            lps = [0]*n
            while i<n:
                if s[i]==s[do_dai]:
                    do_dai+=1
                    lps[i]=do_dai
                    i+=1
                elif do_dai > 0:
                    do_dai = lps[do_dai-1]
                else:
                    lps[i]=0
                    i+=1
            return lps[n-1]
        L = lps(s)
        if L>0 and n%(n-L)==0:
            return True
        else:
            return False
               