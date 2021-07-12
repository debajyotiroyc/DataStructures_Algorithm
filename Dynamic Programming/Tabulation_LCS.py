class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      m,n=len(text1),len(text2)
      l = [[None]*(n+1) for i in range(m+1)]
      for i in range(m+1):
        for j in range(n+1):
          if i==0 or j==0:
            l[i][j]=0
          elif text1[i-1]==text2[j-1]:
            l[i][j]=1+l[i-1][j-1]
          else:
            l[i][j]=max(l[i][j-1],l[i-1][j])
      return l[m][n]
        