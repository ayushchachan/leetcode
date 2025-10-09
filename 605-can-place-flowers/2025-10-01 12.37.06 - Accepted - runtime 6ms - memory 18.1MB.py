class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            return False
        ## length of flowerbed > 1

        i = 0
        j = i + 1

        N = len(flowerbed)

        while i < N - 1:
            if flowerbed[i] == 0:
                if flowerbed[j] == 0:
                    n -= 1
                    i = j + 1
                else:
                    i = j + 2
            else:
                i = j + 1
            
            j = i + 1
        
        if (i == N - 1 
            and flowerbed[i] == 0
            and flowerbed[i - 1] == 0):
            n -= 1
        return n <= 0


