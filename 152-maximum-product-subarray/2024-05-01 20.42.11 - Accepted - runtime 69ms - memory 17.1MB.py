class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product_yet = None
        max_product = float("-inf")
        product_till_negative_number = None
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                max_product_yet = None
                product_till_negative_number = None
                max_product = max(max_product, 0)
            elif num < 0:
                max_product_yet = (
                    (max_product_yet * num) if max_product_yet != None else num
                )
                if product_till_negative_number == None:
                    product_till_negative_number = (max_product_yet,i)
            else:
                max_product_yet = (
                    (max_product_yet * num) if max_product_yet != None else num
                )

            if max_product_yet != None:
                max_product = max(max_product, max_product_yet)
            if (
                product_till_negative_number != None
                and product_till_negative_number[1] < i
            ):
                max_product = max(
                    max_product, max_product_yet / product_till_negative_number[0]
                )

        return int(max_product)

