class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr1 = []
        arr2 = []
        for i in range(1, n+1):
            if i % m == 0:
                continue
            arr1.append(i)
        for j in range(1, n+1):
            if j % m == 0:
                arr2.append(j)
        return sum(arr1) - sum(arr2)