class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # sabse pehele max_sum aur current_sum ko pehele number se start karo 
        max_sum = nums[0]
        current_sum = nums[0]

        # dusre number se lekar end tak ek ek karke check karo 
        for i in range (1,len(nums)):

            # agar abhi wala number apne peeche wala number se bada hai ...
            if nums[i] > nums[i-1]:
                #...toh isse apni purani total current_sum main jod do 
                current_sum += nums[i]
            else:
                #agar bada nahi hai , toh streak tooot gayi and ab nayi total shuru karo is number se
                current_sum = nums[i]
            
            # har step pe check karo ki kya ye nayi total purani wali se badi hai 
            max_sum = max(max_sum, current_sum)

#lastmein jo sabse bada sum mila use return kardo
        return max_sum


    
