from sys import maxint
def maxSubArraySum(a,size):

    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
b = [1, 2, -3, 4, -1, 0]

def kadane(a):
  max_current = max_global = a[0]
  start = 0
  end = 0
  for i in range(1, len(a)):
    max_current = max(a[i], max_current + a[i])
    if (max_current >= max_global):
      max_global = max_current
      end = i
      if (max_global == a[i]): start = i
  return max_global, start, end

def maxZero(a):
  arr_modified = list(map(lambda x: -1 if x == 0 else x, a))
  max, start, end = kadane(arr_modified)
  for i in range(start, end + 1):
    if a[i] == 0: a[i] = 1
    else: a[i] = 0
  return a.count(0)

c = [0, 1, 0, 0, 1, 1, 0]

d = [1,2,3,1]
e = [2,7,9,3,1]
f = [3,1,2,5,4,2]
def rob_brute_wrapper(a):
  def rob_brute(i):
    if (i >= len(a)):
      return 0
    # at each house, ur deciding between stealing it and skip the next house
    # or skipping the current house
    # and make the decision again at the next house
    return max(a[i] + rob_brute(i + 2), rob_brute(i + 1))
  return rob_brute(0)

def rob_1(a):
  max_gold = [a[0], max(a[0], a[1])]

  for i in range(2, len(a)):
    current = a[i]
    preMax = max_gold[i-1]
    twoBackMax = max_gold[i-2]
    max_gold.append(max(current + twoBackMax, preMax))

  return max_gold[len(a)-1]

def rob(a):
  f = [0] * 3
  f[0], f[1] = a[0], max(a[0], a[1])

  for i in range(2, len(a)):
    f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + a[i])

  return f[(len(a) - 1) % 3]



