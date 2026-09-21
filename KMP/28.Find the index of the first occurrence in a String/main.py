class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def lps_build(s):
            n=len(s)
            i=1
            lps = [0]*n
            do_dai = 0
            while i<n:
                if s[i]==s[do_dai]:
                    do_dai+=1
                    lps[i]=do_dai
                    i+=1
                elif do_dai>0:
                    do_dai = lps[do_dai-1] 
                else:
                    lps[i]=0
                    i+=1
            return lps
        def kmp(T,S):
            n=len(T)
            m=len(S)
            rel = []
            lps = lps_build(S)
            i=0
            j=0
            while i<n:
                if S[j]==T[i]:
                    i+=1
                    j+=1
                    if(j==m):
                        rel.append(i-j)
                        j = lps[j-1]
                elif j>0:
                    j=lps[j-1]
                else:
                    i+=1
            return rel
        rel = kmp(haystack,needle)
        if not rel: return -1
        else : return rel[0]                   
                                            