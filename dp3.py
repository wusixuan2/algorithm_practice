class Solution:
    # 先解释为什么10层楼的时候用4次
    # 先从floor4扔
    # break了，就需要用另一个从floor1开始往上找，最多用3次，一共4次
    # 没有break，再从floor7扔
    # break了，就需要用另一个从floor5开始往上找，最多用2次，一共是4次
    # 没有break， 再从floor9扔
    # break了，就需要用另一个从floor8开始往上找，最多用1次，一共是4次
    # 没有break，确定是 k = 10
    # 倒过来看就是一个等差数列的过程：[10], [9, 8], [7, 6, 5], [4, 3, 2, 1]
    # 所以累加的方法就是找到最小的m，使得1到m的公差为1的等差数列的和大于n

    # 然后直接求解就是，等差数列的和为 m * (m + 1) / 2,
    # 令其大于等于 n，
    # 得到 m ** 2 + m - 2n >= 0,
    # 然后用一元二次方程求解公式取正值，
    # 再取ceil()就可以了
    """
    @param n: An integer
    @return: The sum of a and b
    """
    # 累加
    def dropEggs(self, n):
        res = 1
        sum = 1
        while sum < n:
            res += 1
            sum += res
        return res

    # 直接求解
    def dropEggs(self, n):
        return math.ceil((math.sqrt(8 * n) - 1) / 2)

    def dropEggs(self, n):
        import math
        x = int(math.sqrt(n * 2))
        while x * (x + 1) / 2 < n:
            x += 1
        return x

class Solution:
    # 使用滚动数组，加上侯卫东老师在算法强化班中讲解的转移方程
    # dp[i] = max{values[i] - dp[i+1], values[i] + values[i + 1] - dp[i + 2]}

    # 从一亩三分地copy下面这段解释：
    # "令dp[i]为"到游戏结束为止, 在i处先拿的人比后拿的人能够多拿的面值".
    # 如果i处先拿的人只拿1枚, 那么在i处他比对方多拿values[i], 但是在i+1~N处,对手可以比他多拿dp[i+1], 也就是他比对手多拿-dp[i + 1].
    # 因此从i到N, 他比对方多拿values[i] - dp[i+1];同理, 如果先拿的人拿2枚, 那么能比对方多拿values[i] + values[i + 1] - dp[i + 2].
    # 取这二者最大值即可得dp[i], 最后看dp[0] 是大于还是小于0即可."
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False

        n = len(values)
        dp = [0] * 3
        #dp[2] = 0

        for i in range(n-1, -1, -1):
            dp[i%3] = values[i] - dp[(i+1) % 3]
            if i + 2 <= n:
                dp[i%3] = max(dp[i%3], values[i] + values[i+1] - dp[(i+2) % 3])

        return dp[0] >= 0
