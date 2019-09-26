class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        
        dic={}
        
        
        for i in nums2:
            while stack and stack[-1]<i:
                dic[stack.pop()]=i
                
            stack.append(i)
            
            
        
        for i in  stack:
            dic[i]=-1
            
            
        res=[]
        for i in nums1:
            res.append(dic[i])
            
            
        return res
