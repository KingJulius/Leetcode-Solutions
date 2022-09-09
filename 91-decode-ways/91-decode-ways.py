class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        dp[0] = 1 if int(s[0]) != 0 else 0
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1] 
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i-2 if i>1 else 0] 
        return dp[-1]