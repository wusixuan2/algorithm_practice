import heapq
######################## Top K Frequent Words ########################
class Solution:
    # @param {int} k an integer
    def __init__(self, k):
        self.k = k
        self.heap = []

    # @param {int} num an integer
    def add(self, num):
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # if len(h) < k:
        #     heappush(h, num)
        # elif num > h[0]:
        #     heappushpop(h, num)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        return sorted(self.heap, reverse=True)

######################## Top K Frequent Words II ########################
def cmp_words(a, b):
    if a[1] != b[1]:
        return b[1] - a[1]
    return cmp(a[0], b[0])
def cmp(a, b):
    return (a > b) - (a < b)

class HashHeap:
    def __init__(self):
        self.heap = [0]
        self.hash = {}

    def add(self, key, value):
        self.heap.append((key, value))
        self.hash[key] = self.heap[0] + 1
        self.heap[0] += 1
        self._siftup(self.heap[0])

    def remove(self, key):
        index = self.hash[key]
        self._swap(index, self.heap[0])
        del self.hash[self.heap[self.heap[0]][0]]
        self.heap.pop()
        self.heap[0] -= 1
        if index <= self.heap[0]:
            index = self._siftup(index)
            self._siftdown(index)

    def hasKey(self, key):
        return key in self.hash

    def min(self):
        return 0 if self.heap[0] == 0 else self.heap[1][1]

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hash[self.heap[a][0]] = a
        self.hash[self.heap[b][0]] = b

    def _siftup(self, index):
        while index != 1:
            if cmp_words(self.heap[index], self.heap[index // 2]) < 0:
                break
            self._swap(index, index // 2)
            index = index // 2
        return index

    def _siftdown(self, index):
        size = self.heap[0]
        while index < size:
            t = index
            if index * 2 <= size and cmp_words(self.heap[t], self.heap[index * 2]) < 0:
                t = index * 2
            if index * 2 + 1 <= size and cmp_words(self.heap[t], self.heap[index * 2 + 1]) < 0:
                t = index * 2 + 1
            if t == index:
                break
            self._swap(index, t)
            index = t
        return index

    def size(self):
        return self.heap[0]

    def pop(self):
        key, value = self.heap[1]
        self.remove(key)
        return value

class TopK:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here
        self.k = k
        self.top_k = HashHeap()
        self.counts = {}

    # @param {str} word a string
    def add(self, word):
        if word not in self.counts:
            self.counts[word] = 1
        else:
            self.counts[word] += 1

        if self.top_k.hasKey(word):
            self.top_k.remove(word)

        self.top_k.add(word, self.counts[word])

        if self.top_k.size() > self.k:
            self.top_k.pop()

    # @return {str[]} the current top k frequent word
    def topk(self):
        topk = self.top_k.heap[1:]
        topk.sort(cmp=cmp_words)
        return [ele[0] for ele in topk]


######################## Top K Frequent Words II ########################

class Entry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

from bisect import bisect_left
from collections import deque
class TopK:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.top_k = []
        self.mapping = {}

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        if self.k == 0:
            return

        entry = None
        if word in self.mapping:
            entry = self.mapping[word]
            if entry.inTop:
                self.removeFromTop(entry)
            entry.freq += 1
        else:
            self.mapping[word] = Entry(word, 1)
            entry = self.mapping[word]

        self.addToTop(entry)

        if len(self.top_k) > self.k:
            self.top_k[0].inTop = False
            self.top_k.pop(0)


    """
    @return: the current top k frequent words.
    """
    def topk(self):
        if self.k == 0 or len(self.top_k) == 0:
            return []

        results = [e.word for e in self.top_k]
        results.reverse()
        return results


    def addToTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.insert(idx, entry)
        entry.inTop = True


    def removeFromTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.pop(idx)
        entry.inTop = False

######################## Find Median from Data Stream ########################

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        self.minheap, self.maxheap = [], []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians

    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)

        if len(self.minheap) == 0 or len(self.maxheap) ==0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
