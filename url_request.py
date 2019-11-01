import requests

# def getMovieTitles(substr):
#   base_url = "https://jsonmock.hackerrank.com/api/movies/search/?"
#   resp = requests.get(base_url + 'Title=' + substr)
#   j = resp.json()
#   total_pages = j['total_pages']
#   titles = [x['Title'] for x in j['data']]
#   for i in range(2, int(total_pages) + 1):
#     resp = requests.get(base_url + 'Title=' + substr + "&page=" + str(i))
#     j = resp.json()
#     title += [x['Title'] for x in j['data']]
#   return list(sorted(titles))


# def funWithAnagram(s):
#   h, ans = set(), []
#   for word in s:
#     anagram = ''.join(sorted([x for x in word]))
#     if anagram not in h:
#       ans.append(word)
#       h.add(anagram)
#   return list(sorted(ans))




##################
# import json
# def url(title, pageNum = 1):
#   return 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + title + "&page=" + str(pageNum)

# titleArray = []
# data = json.loads(requests.get(url('spiderman')).text)

# totalPage = data["total_pages"]
# for movie in data["data"]:
#   titleArray.append(movie["Title"])
# for page in range(2, totalPage+1):
#   data = json.loads(requests.get(url('spiderman', page)).text)
#   for movie in data["data"]:
#     titleArray.append(movie["Title"])


# print(sorted(titleArray))
####################################

# def reorder(word):
#   return ''.join(sorted([char for char in word]))

# q = ['code', 'ocde', 'ecod','la','lala']
# ans = []
# used_word = set()
# for word in q:
#   word_reorder = reorder(word)
#   if (word_reorder in used_word):
#     continue
#   else:
#     used_word.add(word_reorder)
#     ans.append(word)

# print(ans)
####################################

def maxHeight(wallPositions, wallHeights):
  ans = 0
  for i in range(1, len(wallPositions)):
    dp = wallPositions[i] - wallPositions[i - 1] - 1
    dh = abs(wallHeights[i] - wallHeights[i - 1])
    small = min([wallHeights[i], wallHeights[i - 1]])
    large = max([wallHeights[i], wallHeights[i - 1]])
    if dp == 0:
      continue
    elif dp > dh:
      x = dp - dh
      ans = max(ans, x // 2 + (x & 1) + large)
    else:
      ans = max(ans, dp + small)
    return ans


















