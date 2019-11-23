class HashHeap:

    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def push(self, item):
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)

    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item

    def top(self):
        return self.heap[0]

    def remove(self, item):
        if item not in self.hash:
            return

        index = self.hash[item]
        self._swap(index, self.size - 1)

        del self.hash[item]
        self.heap.pop()

        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = (index - 1) // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i

# from queue import PriorityQueue
import heapq
# or push the negative of the item on the heap, then take the negative again just after you pop the item

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        points = []
        for index, (start, end, height) in enumerate(buildings):
            points.append((start, height, index, True))
            points.append((end, height, index, False))
        points = sorted(points)

        # maxheap = HashHeap(desc=True) # keep track of heights
        maxheap = []
        intervals = []
        last_position = None
        for position, height, index, is_start in points:
            # max_height = maxheap.top()[0] if maxheap.size else 0
            max_height = - maxheap[0][0] if len(maxheap) else 0
            self.merge_to(intervals, last_position, position, max_height)
            if is_start:
                # maxheap.push((height, index))
                heapq.heappush(maxheap, (- height, index))
            else:
                # maxheap.remove((height, index))
                maxheap.remove((- height, index))
            last_position = position

        return intervals

    def merge_to(self, intervals, start, end, height):
        if start is None or height == 0 or start == end:
            return

        if not intervals:
            intervals.append([start, end, height])
            return

        _, prev_end, prev_height = intervals[-1]
        if prev_height == height and prev_end == start:
            intervals[-1][1] = end
            return

        intervals.append([start, end, height])


    ######################## Number of Airplanes in the Sky ########################
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        points = []
        for airplane in airplanes:
            points.append([airplane[0], 1])
            points.append([airplane[1], -1])

        number_of_airplane, max_number_of_airplane = 0, 0
        for _, count_delta in sorted(points):
            number_of_airplane += count_delta
            max_number_of_airplane = max(max_number_of_airplane, number_of_airplane)

        return max_number_of_airplane

    ######################## Top k Largest Numbers ########################
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        self.quick_select(nums, 0, len(nums) - 1, k)
        res =  nums[:k]
        res.sort(reverse=True)
        return res


    def quick_select(self, nums, left, right, k):

        if left == right:
            return

        pivot = nums[left]
        i, j = left, right
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1

            while i <= j and nums[j] < pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


        if j - left + 1 >= k:
            self.quick_select(nums, left, j, k)
        if i - left + 1 <= k:
            self.quick_select(nums, i, right, k - (i - left))

b1=[
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]
]
planes = [(1, 10), (2, 3), (5, 8), (4, 7)] #[[1, 2, 3], [2, 4, 4], [5, 6, 1]]
sol = Solution()
# print(sol.countOfAirplanes(planes))
# print(sol.buildingOutline(b1))

