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
      return length
    ################# Word Break #################
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        maxLen = max([len(w) for w in dict])
        for i in range(1, n + 1):
            for j in range(max(i - maxLen, 0), i):
                print(i,j,dp[j],s[j:i] in dict)
                if not dp[j]:
                    continue
                if s[j:i] in dict:
                  # 如果可以透過dictionary組出0~j的字串(dp[j] == True)
                  # 且s[j:i]在dictionary裡面則可推出dp[i]是True
                    dp[i] = True
                    break #break掉不需要剩下的計算 -> 原因是我們只需要知道有一種方法可以走到i即可
        print(dp)
        return dp[n]
    ################# Word Break II DFS #################
    def wordSearchII(self, board, words):
        res = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.helper(board,words,row,col,set(),res,"")
        return res

    def helper(self, board, words, row, col, used, res, currStr):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return
        if (row,col) in used:
            return
        currStr += board[row][col]
        if currStr in words and currStr not in res:
            res.append(currStr[:])
        #Check if currStr is the prefix of some words. If not, stop searching further
        test = False
        for w in words:
            if w.startswith(currStr):
                test = True
        if test == False:
            return
        #dfs
        used.add( (row,col) )
        self.helper(board, words, row+1, col, used, res, currStr)
        self.helper(board, words, row-1, col, used, res, currStr)
        self.helper(board, words, row, col+1, used, res, currStr)
        self.helper(board, words, row, col-1, used, res, currStr)
        used.remove( (row,col) )
    ################# Word Break II BFS #################
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []

        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    result,
                )

        return list(result)

    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return

        if word in word_set:
            result.add(word)

        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y

            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue

            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result,
            )
            visited.remove((x_, y_))

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

################# Word Break II Trie #################
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode:       #定义字典树的节点
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):    #字典树插入单词
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()   #在此节点申请节点
            node = node.children[c]         #继续遍历
        node.is_word = True
        node.word = word        #存入单词

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None

        return node


class wordSearchIISolution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []

        trie = Trie()
        for word in words:      #插入单词
            trie.add(word)

        result = set()
        for i in range(len(board)):       #遍历字母矩阵，将每个字母作为单词首字母开始搜索
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    trie.root.children.get(c),
                    set([(i, j)]),
                    result,
                )

        return list(result)

    def search(self, board, x, y, node, visited, result):     #在字典树上dfs查找
        if node is None:
            return

        if node.is_word:
            result.add(node.word)

        for delta_x, delta_y in DIRECTIONS:       #向四个方向查找
            x_ = x + delta_x
            y_ = y + delta_y

            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue

            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                node.children.get(board[x_][y_]),
                visited,
                result,
            )
            visited.remove((x_, y_))

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
sol = Solution()
envelop = [[5,4],[6,4],[6,7],[2,3]]
s = "leettcode"
dictionary = ["leett", "code"]
matrix = ["doaf","agai","dcan"]
dictionary = ["dog","dad","dgdg","can","again"]
print(sol.wordSearchII(s, dictionary))






