import random


class HashFunction:

    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap

        return ret


class StandardBloomFilter:

    # @param {int} k an integer
    def __init__(self, k):
        self.bitset = dict()
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))

    # @param {str} word a string
    def add(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            self.bitset[position] = 1


    # @param {str} word a string
    # @return {bool} True if word is exists in bllom filter or false
    def contains(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            if position not in self.bitset:
                return False

        return True

import random


class HashFunction:

    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap

        return ret


class CountingBloomFilter:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here
        self.hashFunc = []
        for i in xrange(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))

        self.bits = [0 for i in xrange(20000)]

    # @param {str} word a string
    def add(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] += 1

    # @param {str} word a string
    def remove(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] -= 1

    # @param {str} word a string
    # @return {bool} True if word is exists in bllom filter or false
    def contains(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            if self.bits[position] <= 0:
                return False

        return True
