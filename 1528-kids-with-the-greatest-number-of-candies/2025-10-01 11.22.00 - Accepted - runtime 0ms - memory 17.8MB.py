class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)
        return result