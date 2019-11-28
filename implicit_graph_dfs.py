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

sol = Solution()
sol.wordPatternMatch("bab","blueredblue")

