class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #k track the position where the next ' valid' element should go 
        k = 0 

        for i in range (len(nums)):
            #if the current element is not the one we want to remove 
            if nums[i] != val:
                #copy it to the "k" position
                nums[k] = nums[i]
                #move the writer forward
                k +=1

        #k also represent the count of element not equal to val
        return k 
        
    

    
        
        