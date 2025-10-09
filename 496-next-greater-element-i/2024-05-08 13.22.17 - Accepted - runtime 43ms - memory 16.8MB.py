class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = {}
        d[nums2[-1]] = len(nums2) - 1
        resArray = [-1] * len(nums2)
        for i in range(len(nums2) - 2, -1, -1):
            if nums2[i + 1] > nums2[i]:
                st.append(nums2[i + 1])
                resArray[i] = nums2[i + 1]
            else:
                while len(st) > 0 and nums2[i] > st[-1]:
                    st.pop()
                if len(st) != 0:
                    resArray[i] = st[-1]
            d[nums2[i]] = i

        res = []
        print(st)
        for i in range(len(nums1)):
            res.append(resArray[d[nums1[i]]])
        return res

