class Stack:
    in_queue = []
    out_queue = []
    def push(self, x):
        self.out_queue.append(x)

    def pop(self):
        self.outSafe()
        return self.out_queue.pop(0)

    def top(self):
        self.outSafe()
        return self.out_queue[0]

    def isEmpty(self):
        self.outSafe()
        return len(self.out_queue) == 0

    # help function, make sure out_queue always has 1 latest added element
    def outSafe(self):
        if len(self.out_queue) == 0 and len(self.in_queue) != 0:
            self.out_queue, self.in_queue = self.in_queue, self.out_queue
        while len(self.out_queue) > 1:
            self.in_queue.append(self.out_queue.pop(0))

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        self.queue = deque([])
        self.size = size
        self.sum = 0.0


    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()

        self.sum += val
        self.queue.append(val)
        return self.sum / len(self.queue)
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def firstUniqChar(self, s):
        dummy = ListNode(None); tail = dummy
        tab, invalid = {}, object()
        for c in s:
            if c not in tab:
                node = ListNode(c)
                tab[c], tail.next, tail = tail, node, node
            else:
                if tab[c] is invalid:
                    continue
                prv, nxt = tab[c], tab[c].next.next
                prv.next = nxt
                if nxt:
                    tab[nxt.val] = prv
                else:
                    tail = prv
                tab[c] = invalid

        return dummy.next.val if dummy.next else '0'

########################## Merge k Sorted Lists ##########################
from heapq import heappush, heappop
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        heap = []
        for h in lists:
            while h:
                heappush(heap, h.val)
                h = h.next
        dummy = ListNode(None)
        h = dummy
        while heap:
            h.next = ListNode(heappop(heap))
            h = h.next
        return dummy.next

########################## Implement Queue by Two Stacks ##########################
class MyQueue:
    def __init__(self, ):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self, ):
        self.top()
        return self.stack2.pop()


    """
    @return: An integer
    """
    def top(self, ):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

########################## K Closest Points ##########################
import heapq

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        self.heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))

            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))

        ret.reverse()
        return ret

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

########################## find the nth number that only have prime factors 2, 3 and 5.##########################
import heapq

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])

        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)

        return val

from heapq import heappush, heappop
class Solution:

    def nthUglyNumber(self, n):

        h = [(1,1)]

        for _ in range(n):

            num, m = heappop(h)
            for f in [2, 3, 5]:
                if f >= m:
                    heappush(h, (f*num, f))
        return num
