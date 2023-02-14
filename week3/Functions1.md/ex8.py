def spy_game(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+1]==7:
            return True
        
    
    return False
    
a = [int(s) for s in input().split()]

print(spy_game(a))