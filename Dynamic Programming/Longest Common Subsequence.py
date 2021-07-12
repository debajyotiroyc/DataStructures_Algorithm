class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      if len(text1) == 0 or len(text2) == 0:
        return 0
      elif text1[-1]==text2[-1]:
        return 1+self.longestCommonSubsequence(text1[:len(text1)-1],text2[:len(text2)-1])
      else:
        return max(self.longestCommonSubsequence(text1[:len(text1)-1],text2[:len(text2)]),
                  self.longestCommonSubsequence(text1[:len(text1)],text2[:len(text2)-1]))