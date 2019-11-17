import math

def twoSum(a, target):
  dictNum = dict()
  for i in range(len(a)):
    if (a[i] in dictNum):
      return dictNum[a[i]], i

    dictNum[target - a[i]]= i
  return -1

def threeSum(a, target):
  for i in range(len(a)-2):
    dictNum = dict()
    for j in range(i+1, len(a)):
      print(i,j, dictNum)
      if (a[j] in dictNum):
        return i, dictNum[a[j]], j
      dictNum[target - a[i] - a[j]]= j
  return -1


def twoDiff(a, target):
  hashmap = dict()
  for i in range(len(a)):
    if (a[i] in hashmap):
      return hashmap[a[i]], i
    hashmap[a[i] - target]= i
    hashmap[a[i] + target]= i
  return -1
def twoSquareDiff(a, target):
  hashmap = dict()
  for i in range(len(a)):
    if (a[i] in hashmap):
      return hashmap[a[i]], i
    hashmap[math.sqrt(abs(a[i]*a[i] - target))]= i
    hashmap[math.sqrt(a[i]*a[i] + target)]= i
  return -1








