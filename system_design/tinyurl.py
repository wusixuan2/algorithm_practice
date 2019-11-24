class TinyUrl:

    def __init__(self):
        self.dict = {}

    def getShortKey(self, url):
        return url[-6:]

    def idToShortKey(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            s = ch[id % 62] + s
            id /= 62
        while len(s) < 6:
            s = 'a' + s
        return s

    def shortkeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id

    # @param {string} url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, url):
        # Write your code here
        ans = 0
        for a in url:
            ans = (ans * 256 + ord(a)) % 56800235584L

        while ans in self.dict and self.dict[ans] != url:
            ans = (ans + 1) % 56800235584L

        self.dict[ans] = url
        return "http://tiny.url/" + self.idToShortKey(ans)

    # @param {string} url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, url):
        # Write your code here
        short_key = self.getShortKey(url)
        return self.dict[self.shortkeyToid(short_key)]

class TinyUrl2:
    def __init__(self):
        self.l2s = {}
        self.s2l = {}
        self.cnt = 0
        self.tinyUrl = 'http://tiny.url/'
        self.charset = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

    def newShortUrl(self):
        res = ''
        tmp = self.cnt
        for i in range(6):
            res += self.charset[tmp % 62]
            tmp //= 62
        self.cnt += 1
        return self.tinyUrl + res

    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def createCustom(self, long_url, key):
        short_url = self.tinyUrl + key
        if long_url in self.l2s:
            if self.l2s[long_url] == short_url:
                return short_url
            else:
                return 'error'
        if short_url in self.s2l:
            return 'error'
        self.l2s[long_url] = short_url
        self.s2l[short_url] = long_url
        return short_url

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, long_url):
        if long_url in self.l2s:
            return self.l2s[long_url]
        short_url = self.newShortUrl()
        self.l2s[long_url] = short_url
        self.s2l[short_url] = long_url
        return short_url

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        if short_url in self.s2l:
            return self.s2l[short_url]
        else:
            return 'error'
