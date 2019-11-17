import sys
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
        # 在 first position of target 的情况下不会出现死循环
        # 但是在 last position of target 的情况下会出现死循环
        # 样例：nums=[1，1] target = 1
        # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接 // 2 就可以了
            # java和C++ 最好写成 mid = start + (end - start) / 2
            # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
            mid = (start + end) // 2

            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
            if nums[mid] < target:
                # 写作 start = mid + 1 也是正确的
                # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
                # 不写的好处是，万一你不小心写成了 mid - 1 你就错了
                # start = mid
                start = mid + 1
            elif nums[mid] == target:
                end = mid
            else:
                # 写作 end = mid - 1 也是正确的
                # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
                # 不写的好处是，万一你不小心写成了 mid + 1 你就错了
                # end = mid
                end = mid - 1

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


    ############## 三步翻转法 recover rotated sorted array ##############
    # 找到第一个比后面的数大的数，以[4,5,1,2,3]为例，找到5，翻转[4,5]得到[5,4]，翻转[1,2,3]得到[3,2,1]
    # 最后翻转[5,4,3,2,1]得到[1,2,3,4,5]
    def recoverRotatedSortedArray(self, array):
      for i in range(len(array)-1):
        if array[i] > array[i + 1]:
          self.reverse_section(array, 0, i)
          self.reverse_section(array, i + 1, len(array) - 1)
          self.reverse_section(array, 0, len(array) - 1)

      return array

    def reverse_section(self, array, start, end):
      while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start+=1
        end-=1

    ############## 二维矩阵找数问题Search a 2D Matrix II ##############
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return 0

        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return count

    ############## Median of Two Sorted Arrays ##############

    # findMedian -> findKth
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays1(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + bigger) / 2

    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b  + k - 1]
        if len(B) == index_b:
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])

        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None

        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)


    # 二分答案的办法
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays1(self, A, B):
        # write your code here
        len_a, len_b = len(A), len(B)
        if (len_a + len_b) % 2 == 1:
            return self.finf_kth(A, B, (len_a + len_b) // 2 + 1)
        else:
            left = self.finf_kth(A, B, (len_a + len_b) // 2 )
            right = self.finf_kth(A, B, (len_a + len_b) // 2 + 1)
            return (left + right) / 2

    def finf_kth(self, A, B, k):
        if len(A) == 0:
            left, right = B[0], B[-1]
        elif len(B) == 0:
            left, right = A[0], A[-1]
        else:
            left, right = min(A[0], B[0]), max(A[-1], B[-1])
        while left + 1 < right:
            mid = (left + right) // 2
            count1 = self.helper(A, mid)
            count2 = self.helper(B, mid)
            if count1 + count2 < k:
                left = mid
            else:
                right = mid
        count1 = self.helper(A, left)
        count2 = self.helper(B, left)
        if count1 + count2 >= k:
            return left
        else:
            return right

    def helper(self, array, flag):
        if len(array) == 0:
            return 0
        left, right = 0 ,len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= flag:
                left = mid
            else:
                right = mid
        if array[right] <= flag:
            return right + 1
        if array[left] <= flag:
            return left + 1
        return 0

    # merge sort 加 binary search O(log(n))
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)

        # border cases
        if (m > n): return self.findMedianSortedArrays(B, A)
        if m == 0:
          return (B[(n - 1)//2] + B[n//2]) / 2
        if m == 1:
          for i in range(n):
            if A[0] < B[i]:
              B.insert(i, A[0])
            elif (i == n-1):
              B.append(A[0])
          return (B[n//2] + B[(n+1)//2]) / 2 # len of B is n+1

        if A[m - 1] < B[0]:
          A.extend(B)
          return (A[(m+n - 1)//2] + A[(m+n)//2]) / 2
        if A[0] > B[n - 1]:
          B.extend(A)
          return (B[(m+n - 1)//2] + B[(m+n)//2]) / 2

        # binary
        start = 0
        end = m - 1

        while start <= end:
          cutA = (start + end) // 2
          L1 = A[cutA]
          R1 = A[cutA + 1]

          cutB = (m + n + 1)//2 - cutA - 1 # 奇偶cases不一样，所以m + n + 1
          L2 = B[cutB - 1]
          R2 = B[cutB]

          if L1 > R2:
            end = cutA - 1
          elif L2 > R1:
            start = cutA + 1
          else:
            if ((m+n) % 2 == 0):
              return (max(L1,L2) + min(R1, R2)) / 2
            return max(L1, L2)

sol = Solution()
a = [1,3,9,10]
b = [1,4,6,6,10,11]

a = [1,1,14,31,33,40,42,66,71,74,113,117,124,125,127,137,143,184,187,188,221,222,224,248,251,269,293,294,315,324,330,353,358,366,368,389,389,408,424,432,433,451,452,456,459,475,480,483,484,496,509,515,519,523,559,567,568,593,598,600,612,623,626,628,632,633,634,646,654,663,681,696,706,709,717,723,746,753,790,790,798,824,826,847,849,857,866,879,882,894,894,913,925,938,942,961,974,988,988,989,998]
b = [3,4,5,6,9,15,17,20,21,21,23,25,27,27,28,29,31,32,37,41,43,47,49,50,52,52,52,54,59,60,67,68,71,72,73,77,78,84,86,88,88,91,94,98,98,98,100,102,105,106,107,107,110,117,118,120,122,124,126,129,131,134,135,144,147,154,158,158,163,164,164,170,171,171,172,172,176,178,180,183,184,185,189,196,197,199,200,200,204,208,214,217,223,226,227,231,231,232,232,237,243,244,245,251,258,259,266,271,274,277,279,280,280,281,283,284,284,284,286,288,290,296,299,301,302,302,302,303,305,308,308,309,311,313,313,316,322,323,326,327,328,329,331,331,337,340,340,342,343,345,346,349,349,349,350,354,366,366,375,376,377,377,379,382,389,390,391,392,393,394,397,397,397,399,400,400,402,402,403,404,405,405,408,414,415,416,416,416,419,421,422,426,426,427,430,432,433,436,440,443,445,448,448,454,455,456,456,457,458,459,459,462,465,466,467,471,475,493,500,501,505,507,509,511,512,512,513,513,514,514,515,516,517,518,520,521,523,524,525,528,533,535,535,536,537,539,542,542,544,545,547,551,552,553,554,554,556,557,557,558,559,559,561,563,565,568,570,578,578,579,580,580,581,581,588,590,591,592,592,593,594,595,597,601,603,603,605,607,610,611,612,612,612,614,617,620,621,622,622,624,624,625,625,627,627,627,632,635,635,637,638,642,644,644,647,647,650,651,652,653,654,655,657,660,664,667,670,671,672,673,673,676,677,682,685,685,686,686,688,694,695,695,697,699,700,700,704,704,707,709,713,713,715,716,716,717,719,721,725,732,736,740,742,745,746,749,752,754,755,756,756,757,760,762,763,765,766,768,768,768,772,774,775,775,780,784,784,785,785,788,790,791,792,794,796,796,798,800,802,802,804,806,806,808,813,814,816,817,817,818,824,824,825,825,827,830,832,834,834,837,841,842,843,845,846,848,852,855,855,855,860,861,866,866,872,874,875,875,877,883,886,892,892,895,895,897,898,898,900,900,900,904,904,905,906,907,909,909,914,914,914,915,922,924,927,928,930,931,936,938,939,941,944,945,946,947,948,950,955,956,960,961,967,967,969,971,972,978,979,981,982,984,984,989,990,993,997,999,999,1001]
# print(sol.findMedianSortedArrays(a, b))
