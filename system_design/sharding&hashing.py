# Take id to 360. If there are 3 machines at the beginning, then let 3 machines be responsible for the three parts of 0~119, 120~239, 240~359. Then, how much is the model, check which zone you are in, and which machine to go to.
# When the machine changes from n to n+1, we find the largest one from the n intervals, then divide it into two and give half to the n+1th machine.
# For example, when changing from 3 to 4, we find the third interval 0~119 is the current largest interval, then we divide 0~119 into 0~59 and 60~119. 0~59 is still given to the first machine, 60~119 to the fourth machine.
# Then change from 4 to 5, we find the largest interval is the third interval 120~239, after splitting into two, it becomes 120~179, 180~239.
# [x, (x + y) / 2, z] and [(x + y) / 2 + 1, y, n]
class Solution:
    # @param {int} n a positive integer
    # @return {int[][]} n x 3 matrix
    def consistentHashing(self, n):
        results = [[0, 359, 1]]
        for i in range(1, n):
            index = 0
            for j in range(i):
                if results[j][1] - results[j][0] + 1 > \
                   results[index][1] - results[index][0] + 1:
                    index = j

            x, y = results[index][0], results[index][1]
            results[index][1] = (x + y) / 2
            results.append([(x + y) / 2 + 1, y, i + 1])

        return results
