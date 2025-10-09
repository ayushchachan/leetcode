class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottles_drunk = 0
        empty_bottles = 0

        while numBottles > 0 or empty_bottles >= numExchange:
            bottles_drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0

            while empty_bottles >= numExchange:
                numBottles += 1
                empty_bottles -= numExchange
                numExchange += 1
        return bottles_drunk

