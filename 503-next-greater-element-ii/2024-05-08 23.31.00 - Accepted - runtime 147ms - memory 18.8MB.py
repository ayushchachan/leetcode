class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        res = [-1] * len(nums)
        i = len(nums) - 1
        j = 0
        while i > -1:
            if len(st) == 0:
                if j >= i:
                    res[i] = -1
                    st.append((nums[i], i))
                    i -= 1
                    continue
                while nums[j] <= nums[i]:
                    j += 1
                    if j == i:
                        break
                if j == i:
                    res[i] = -1
                    st.append((nums[i], i))
                else:
                    res[i] = nums[j]
                    st.append((res[i], j % len(nums)))
                    st.append((nums[i], i))
                    j += 1
                i -= 1
            else:
                lastEle = None
                while len(st) != 0 and st[-1][0] <= nums[i]:
                    lastEle = st.pop()
                if len(st) == 0:
                    continue
                else:
                    res[i] = st[-1][0]
                    st.append((nums[i], i))
                    i -= 1

        return res

