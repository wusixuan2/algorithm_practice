class FriendshipService:

    def __init__(self):
        # initialize your data structure here.
        self.followers = dict()
        self.followings = dict()


    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowers(self, user_id):
        if user_id not in self.followers:
            return []
        results = list(self.followers[user_id])
        results.sort()
        return results

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowings(self, user_id):
        if user_id not in self.followings:
            return []
        results = list(self.followings[user_id])
        results.sort()
        return results

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id follows to_user_id
    def follow(self, to_user_id, from_user_id):
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        self.followers[to_user_id].add(from_user_id)

        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followings[from_user_id].add(to_user_id)

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id unfollows to_user_id
    def unfollow(self, to_user_id, from_user_id):
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)

        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)

########################### Memcache ###########################
# 1.get(curtTime, key). 得到key的值，如果不存在返回2147483647
# 2.set(curtTime, key, value, ttl). 设置一个pair(key,value)，有效期从curtTime到curtTime + ttl -1 , 如果ttl为0，则一直存在
# 3.delete(curtTime, key). 删除这个key
# 4.incr(curtTime, key, delta). 给key的value加上delta，并且返回 如果不存在返回 2147483647。
# 5.decr(curtTime, key, delta). 给key的value减去delta，并且返回 如果不存在返回 2147483647。

class Resource:

    def __init__(self, value, expired):
        self.value = value
        self.expired = expired

INT_MAX = 0x7fffffff

class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.client = dict()

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        if key not in self.client:
            return INT_MAX
        res = self.client.get(key)
        if res.expired >= curtTime or res.expired == -1:
            return res.value
        else:
            return INT_MAX

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        if ttl:
            res = Resource(value, curtTime + ttl - 1)
        else:
            res = Resource(value, -1)

        self.client[key] = res

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        if key not in self.client:
            return

        del self.client[key]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value += delta

        return self.client[key].value

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value -= delta

        return self.client[key].value

########################### LRU Cache (Least Recently Used) ###########################
class LinkedNode:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
# We will use "dummy" nodes for the "head" and "tail". This will let us omit head == null checks for adding to the list, which also improves performance on the common operation of inserting into our list.
# This class will be used to maintain ordering. The 1st element in the list represents the most "recently used" Node.
# We create a Doubly-Linked instead of Singly-Linked list so that, given access to a Node in the list, we can remove it.
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):    #将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return

        # remove the current node from linked list
        prev.next = node.next
        # update the previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)

    # @return an integer
    def get(self, key):   #获取数据
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):     #数据放入缓存
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return

        self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
        if len(self.key_to_prev) > self.capacity:   #如果缓存超出上限
            self.pop_front()          #删除头部


########################### Mini Cassandra ###########################
# Cassandra is a NoSQL database (a.k.a key-value storage). One individual data entry in cassandra constructed by 3 parts:

# 1. row_key. (a.k.a hash_key, partition key or sharding_key.)
# 2. column_key 3.value
# row_key is used to hash and can not support range query. Let's simplify this to a string.
# column_key is sorted and support range query. Let's simplify this to integer.
# value is a string. You can serialize any data into a string and store it in value.
# 一个 row_key 可以对应多个 Column; 而一个 row_key 和一个 column_key 是唯一确定对应的 value 的.

class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

from collections import OrderedDict


class MiniCassandra:

    def __init__(self):
        # initialize your data structure here.
        self.hash = {}

    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
    def insert(self, raw_key, column_key, column_value):
        if raw_key not in self.hash:
            self.hash[raw_key] = OrderedDict()
        self.hash[raw_key][column_key] = column_value

    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns

    def query(self, raw_key, column_start, column_end):
        result = []
        if raw_key not in self.hash:
            return result

        for i in range(column_start, column_end+1):
            if i in self.table[raw_key]:
                result.append(Column(i, self.table[raw_key][i]))

        # self.hash[raw_key] = OrderedDict(sorted(self.hash[raw_key].items()))
        # for key, value in self.hash[raw_key].items():
        #     if key >= column_start and key <= column_end:
        #         rt.append(Column(key, value))

        return result
