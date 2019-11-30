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
