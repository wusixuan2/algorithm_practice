s1 = "kkkk"
s2 = "ifailuhkqq"
def sherlockAndAnagrams(s):
    res = 0
    for l in range(1, len(s)):
        cnt = {}
        for i in range(len(s) - l + 1):
            subs = list(s[i:i + l])
            subs.sort()
            subs = ''.join(subs)
            if subs in cnt:
                cnt[subs] += 1
            else:
                cnt[subs] = 1
            res += cnt[subs] - 1
    return res
from collections import Counter
def sherlockAndAnagrams(s):
  count = 0
  for i in range(1, len(s)+1):
    # a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i + 1)]
    for j in range(len(s)-i + 1):
      a = "".join(sorted(s[j:j+i]))
      print("a",s[j:j+i],a)
    b = Counter(a)
    print("b",b)
    for j in b:
      print('b[j]',b[j])
      count+=b[j]*(b[j]-1)/2
      print('count',count)
  return int(count)
print(sherlockAndAnagrams(s2))
