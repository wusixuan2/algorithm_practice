'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''
class GFSClient(BaseGFSClient):

    # @param {int} chunkSize chunk size bytes
    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        # initialize your data structure here
        self.chunkSize = chunkSize
        self.chunkNum = dict()


    # @param {str} filename a file name
    # @return {str} conetent of the file given from GFS
    def read(self, filename):
        # Write your code here
        if filename not in self.chunkNum:
            return None
        content = ''
        for index in xrange(self.chunkNum.get(filename)):
            sub_content = BaseGFSClient.readChunk(self, filename, index)
            if sub_content:
                content += sub_content

        return content


    # @param {str} filename a file name
    # @param {str} content a string
    # @return nothing
    def write(self, filename, content):
        # Write your code here
        length = len(content)
        chunkNum = (length - 1) / self.chunkSize + 1
        self.chunkNum[filename] = chunkNum
        for index in xrange(chunkNum):
            sub_content = content[index * self.chunkSize :
                                  (index + 1) * self.chunkSize]
            BaseGFSClient.writeChunk(self, filename, index, sub_content)


class HeartBeat:

    def __init__(self):
        # initialize your data structure here
        self.slaves_ip_list = dict()


    # @param {str[]} slaves_ip_list a list of slaves'ip addresses
    # @param {int} k an integer
    # @return nothing
    def initialize(self, slaves_ip_list, k):
        self.k = k
        for ip in slaves_ip_list:
            self.slaves_ip_list[ip] = 0


    # @param {int} timestamp current timestamp in seconds
    # @param {str} slave_ip the ip address of the slave server
    # @return nothing
    def ping(self, timestamp, slave_ip):
        if slave_ip not in self.slaves_ip_list:
            return

        self.slaves_ip_list[slave_ip] = timestamp


    # @param {int} timestamp current timestamp in seconds
    # @return {str[]} a list of slaves'ip addresses that died
    def getDiedSlaves(self, timestamp):
        results = []
        for ip, time in self.slaves_ip_list.items():
            if time <= timestamp - 2 * self.k:
                results.append(ip)
        return results
