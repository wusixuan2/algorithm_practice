class Solution:
    # @param {int[][]} envelopes a number of envelopes with widths and heights
    # @return {int} the maximum number of envelopes
    def maxEnvelopes(self, envelopes):
      # 第二个维度 height 降序
      # key function transforms each element before sorting, it takes the value and returns 1 value which is then used within sort instead of the original value
      height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
      dp, length = [0] * len(height), 0

      import bisect
      for h in height:
          i = bisect.bisect_left(dp, h, 0, length)

          dp[i] = h
          if i == length:
              length += 1
          print(i,dp)
      return length

sol = Solution()
envelop = [[5,4],[6,4],[6,7],[2,3]]
# print(sol.maxEnvelopes(envelop))
