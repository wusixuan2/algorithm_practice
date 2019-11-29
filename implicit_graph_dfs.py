KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, '', results)

        return results

    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return

        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)

    # Word Pattern
    """
    @param pattern: a string,denote pattern string
    @param str: a string,denote matching string
    @return: return an boolean,denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        words = teststr.split()

        if len(words) != len(pattern):
            return False

        c_2_w, w_2_c = {}, {}
        for c, w in zip(pattern, words):
            if c in c_2_w and c_2_w[c] != w:
                return False
            c_2_w[c] = w

            if w in w_2_c and w_2_c[w] != c:
                return False
            w_2_c[w] = c

        return True

    # Word Pattern II - dfs
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        return self.is_match(pattern, string, {}, set())

    def is_match(self, pattern, string, mapping, used):
        if not pattern:
            return not string

        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_match(pattern[1:], string[len(word):], mapping, used)

        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue

            used.add(word)
            mapping[char] = word

            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True

            del mapping[char]
            used.remove(word)

        return False

# Recursion
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])

        if nums is None:
            return []

        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result

# Non-Recursion
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None:
            return []
        if nums == []:
            return [[]]
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations

    ##############################################
    # Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.
    def splitString(self, s):
        # write your code here
        result = []
        self.dfs(result, [], s)
        return result

    def dfs(self, result, path, s):
        if s == "":
            result.append(path[:]) #important: use path[:] to clone it
            return
        for i in range(2):
            if i+1 <= len(s):
                path.append(s[:i+1])
                self.dfs(result, path, s[i+1:])
                path.pop()

    ##############################################
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()

    ##############################################
    # Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()

    ##############################################
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    # 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 combination 拼起来放到 results 里
    # （找到所有以 combination 开头的满足条件的组合，放到 results）
    def dfs(self, candidates, target, start, combination, results):
        # 递归的出口：target <= 0
        if target < 0:
            return

        if target == 0:
            # deepcooy
            return results.append(list(combination))

        # 递归的拆解：挑一个数放到 combination 里
        for i in range(start, len(candidates)):
            # [2] => [2,2]
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2,2] => [2]
            combination.pop()  # backtracking
    ##############################################
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        candidates.sort()
        self.ans, tmp, use = [], [], [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, tmp, use)
        return self.ans
    def dfs(self, can, target, p, now, tmp, use):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p, len(can)):
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):
                tmp.append(can[i])
                use[i] = 1
                self.dfs(can, target, i+1, now + can[i], tmp, use)
                tmp.pop()
                use[i] = 0

from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}

        self.bfs(end, distance, dict)

        results = []
        self.dfs(start, end, distance, dict, [start], results)

        return results

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words

    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return

        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()










