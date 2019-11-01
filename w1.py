import math
import re

palindrome2 = "abaaba"
palindrome3 = "aa"
palindrome1 = "abccccdd"

def longestPalindrome(s):
  if not s:
      return ""

  n = len(s)
  is_palindrome = [[False] * n for _ in range(n)]

  for i in range(n):
      is_palindrome[i][i] = True
  for i in range(1, n):
      is_palindrome[i][i - 1] = True

  longest, start, end = 1, 0, 0
  for length in range(1, n):
      for i in range(n - length):
          j = i + length
          is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
          if is_palindrome[i][j] and length + 1 > longest:
              longest = length + 1
              start, end = i, j

  return s[start:end + 1]


def longestPalindromeBuild(str):
  charSet = set()
  max = 0
  for i in range(len(str)):
    if (str[i] in charSet):
      charSet.remove(str[i])
      max += 2
    else:
      charSet.add(str[i])

  if len(charSet) > 0:
    max += 1
  return max
def longestPalindromeBuild(self, s):
  hash = {}

  for c in s:
    if c in hash:
      del hash[c]
    else:
      hash[c] = True

  remove = len(hash)
  if remove > 0:
    remove -= 1

  return len(s) - remove

source1 = "sourse"
target1= "target"
target2 = "hat"
source2 = "lalalallahatlalalal"

# source.find(target)
def subStr(source, target):

  if source == None or target == None or len(source) < len(target):
    return -1

  for i in range(len(source)-len(target)+1):
    if target == source[i:len(target)+i]:
      return i
  return -1

def validPalindrome(str):
  str = re.sub(r'\W', '', str)
  if (not str): return True

  for i in range (len(str)//2):
    if str[i].lower() == str[-i-1].lower():
      continue
    else:
      return False
  return True


def longestPalindrome(s):
  ans = ''

  for i in range(len(s) * 2 - 1):
    l = i // 2
    r = l + i % 2

    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1

    ans = max(ans, s[l+1:r], key=len)
  return ans

def longestPalindrome(s):
  if not s:
      return

  # Using manacher's algorithm
  # abba => #a#b#b#a#
  chars = []
  for c in s:
      chars.append('#')
      chars.append(c)
  chars.append('#')

  n = len(chars)
  palindrome = [0] * n
  palindrome[0] = 1

  mid, longest = 0, 1
  for i in range(1, n):
      length = 1
      if mid + longest > i:
          mirror = mid - (i - mid)
          length = min(palindrome[mirror], mid + longest - i)

      while i + length < len(chars) and i - length >= 0:
          if chars[i + length] != chars[i - length]:
              break;
          length += 1

      if length > longest:
          longest = length
          mid = i

      palindrome[i] = length

  # remove the extra #
  longest = longest - 1
  start = (mid - 1) // 2 - (longest - 1) // 2
  return s[start:start + longest]

# print(longestPalindrome(palindrome2))

def manacher(s):
    #预处理
    s='#'+'#'.join(s)+'#'

    RL=[0]*len(s)
    MaxRight=0
    pos=0
    MaxLen=0
    for i in range(len(s)):
        if i<MaxRight:
            RL[i]=min(RL[2*pos-i], MaxRight-i)
        else:
            RL[i]=1
        #尝试扩展，注意处理边界
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        #更新MaxRight,pos
        if RL[i]+i-1>MaxRight:
            MaxRight=RL[i]+i-1
            pos=i
        #更新最长回文串的长度
        MaxLen=max(MaxLen, RL[i])
    return MaxLen-1
