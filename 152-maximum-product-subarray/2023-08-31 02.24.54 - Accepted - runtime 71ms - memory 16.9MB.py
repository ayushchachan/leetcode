class Solution:
    def maxProduct(self, nums) -> int:
        maxP = nums[0]
        sIndex = 0;
        for i in range(len(nums)):
            if(nums[i] == 0):
                if(i != 0):
                    maxP = max(self.getMaxProduct(sIndex,i - 1,nums),maxP)
                sIndex = i + 1
        if(sIndex < len(nums)):
            maxP =  max(maxP,self.getMaxProduct(sIndex,len(nums) - 1,nums))
        return maxP
    def getMaxProduct(self,sIndex,lIndex,nums):
        if(len(nums) == 1):
            return nums[0]
        i = sIndex;j = lIndex
        nCount = 0
        leftP = 0;rightP = 0
        #-ve int count
        product = 1;
        for index in range(i,j + 1):
            if(nums[index] < 0):
                nCount += 1
            product = product * nums[index]
        if(nCount % 2 == 0):
            return product
        else:
            #calculate leftP
            
            nCountTemp = 0
            leftIndex = i
            while(True):
                if(nums[leftIndex] < 0):
                    nCountTemp += 1
                    if(nCountTemp == nCount):
                        break
                
                leftP = (leftP if leftP != 0 else 1) * nums[leftIndex]
                # print("leftP : ",  leftP,leftIndex)
                leftIndex += 1
            
            #calculate rightP
            
            nCountTemp = 0
            rightIndex = j
            while(True):
                if(nums[rightIndex] < 0):
                    nCountTemp += 1
                    if(nCountTemp == nCount):
                        break
                rightP = (rightP if rightP != 0 else 1) * nums[rightIndex]
                # print("rightP : ",  rightP,rightIndex)
                rightIndex -= 1
            
            return max(leftP,rightP)

        
print(Solution().maxProduct([2,-5,-2,-4,3,0]))

        