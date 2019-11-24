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

    # After adding a machine, the data comes from one of the machines. The read load of this machine is too large, which will affect the normal service.
    # When adding to 3 machines, the load of each server is not balanced, it is 1:1:2
    # From 0~359 to a range of 0 ~ n-1, the interval is connected end to end and connected into a circle.
    # When joining a new machine, randomly choose to sprinkle k points in the circle, representing the k micro-shards of the machine.
    # Each data also corresponds to a point on the circumference, which is calculated by a hash function.
    # Which machine belongs to which data is to be managed is determined by the machine to which the first micro-shard point that is clockwise touched on the circle is corresponding to the point on the circumference of the data.
    # 在 Consistent Hashing I 中我们介绍了一个比较简单的一致性哈希算法，这个简单的版本有两个缺陷：

    # 增加一台机器之后，数据全部从其中一台机器过来，这一台机器的读负载过大，对正常的服务会造成影响。
    # 当增加到3台机器的时候，每台服务器的负载量不均衡，为1:1:2。
    # 为了解决这个问题，引入了 micro-shards 的概念，一个更好的算法是这样：

    # 将 360° 的区间分得更细。从 0~359 变为一个 0 ~ n-1 的区间，将这个区间首尾相接，连成一个圆。
    # 当加入一台新的机器的时候，随机选择在圆周中撒 k 个点，代表这台机器的 k 个 micro-shards。
    # 每个数据在圆周上也对应一个点，这个点通过一个 hash function 来计算。
    # 一个数据该属于哪台机器负责管理，是按照该数据对应的圆周上的点在圆上顺时针碰到的第一个 micro-shard 点所属的机器来决定。
    # n 和 k在真实的 NoSQL 数据库中一般是 2^64 和 1000。
    # @param {int} n a positive integer
    # @param {int} k a positive integer
    # @return {Solution} a Solution object
    @classmethod
    def create(cls, n, k):
        # Write your code here
        solution = cls()
        solution.ids = {}
        solution.machines = {}
        solution.n = n
        solution.k = k
        return solution

    # @param {int} machine_id an integer
    # @return {int[]} a list of shard ids
    def addMachine(self, machine_id):
        # write your code here
        ids = []
        import random
        for i in range(self.k):
            index = random.randint(0, self.n - 1)
            while index in self.ids:
                index = random.randint(0, self.n - 1)

            ids.append(index)
            self.ids[index] = True

        ids.sort()
        self.machines[machine_id] = ids
        return ids

    # @param {int} hashcode an integer
    # @return {int} a machine id
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        machine_id = -1
        distance = self.n + 1

        for key, value in self.machines.items():
            import bisect
            index = bisect.bisect_left(value, hashcode) % len(value)
            d = value[index] - hashcode
            if d < 0:
                d += self.n

            if d < distance:
                distance = d
                machine_id = key

        return machine_id
class LoadBalancer:

    def __init__(self):
        self.server_ids = []
        self.id2index = {}

    # @param {int} server_id add a new server to the cluster
    # @return nothing
    def add(self, server_id):
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1

    # @param {int} server_id remove a bad server from the cluster
    # @return nothing
    def remove(self, server_id):
        if server_id not in self.id2index:
            return

        # remove the server_id
        index = self.id2index[server_id]
        del self.id2index[server_id]

        # overwrite the one to be removed
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    # @return {int} pick a server in the cluster randomly with equal probability
    def pick(self):
        import random
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]

class WebLogger:

    def __init__(self):
        self.Q = []

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        self.Q.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        if self.Q == []:
            return 0
        i = 0
        n = len(self.Q)
        while i < n and self.Q[i] + 300 <= timestamp:
            i += 1
        self.Q = self.Q[i:]
        return len(self.Q)

# cache优化，使用多级bucket储存，获得结果的时候分别从day，hour，minute，second对应的Map里面取，减少访问Memory的次数
class RateLimiter:

    def __init__(self):
        # do some intialize if necessary
        self.mp = {}

    # @param {int} timestamp the current timestamp
    # @param {string} event the string to distinct different event
    # @param {string} rate the format is [integer]/[s/m/h/d]
    # @param {boolean} increment whether we should increase the counter
    # @return {boolean} true or false to indicate the event is limited or not
    def is_ratelimited(self, timestamp, event, rate, increment):
        # Write your code here
        start = rate.find("/")
        total_time = int(rate[:start])
        type = rate[start+1:]

        time = 1
        if type == 'm':
            time *= 60
        elif type == 'h':
            time = time * 60 * 60
        elif type == 'd':
            time = time * 60 * 60 * 24
        last_time = timestamp - time + 1

        if event not in self.mp:
            self.mp[event] = []

        rt = self.find_event(self.mp[event], last_time) >= total_time
        if increment and not rt:
            self.insert_event(self.mp[event], timestamp)

        return rt

    def insert_event(self, event, timestamp):
        event.append(timestamp)

    def find_event(self, event, last_time):
        l, r = 0, len(event) - 1
        if r < 0 or event[r] < last_time:
            return 0

        ans = 0
        while l <=r:
            mid = (l + r) >> 1
            if event[mid] >= last_time:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return len(event) - 1 - ans + 1
