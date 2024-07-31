# %%

def removeElement(nums, val):
    k = len(nums)
    i = 0
    while val in nums:
        if nums[i] == val:
            del nums[i]
            k -= 1
            i = i
        else:
            pass
            i += 1
            
    return k

def check_output(nums, val, expectedNums): 
    '''
    nums:
    val: 
    expectedNums: The expected answer with correct length.
    '''

    k = removeElement(nums, val) # // Calls your implementation

    assert k == len(expectedNums)

    nums[0:k].sort()  # Sort the first k elements of nums
    # expectedNums.sort() # It is sorted with no values equaling val.
    print(f'num: {nums}\n exceptedNums: {exceptedNums}')
    for i in range(k) :    
        assert nums[i] == expectedNums[i], f'excepted: {exceptedNums[i]}, val: {nums[i]}'
    
# %%
nums =  [0,1,2,2,3,0,4,2]
val = 2
exceptedNums = [0, 1, 4, 0, 3]
# %%
check_output(nums=nums, val=val, expectedNums=exceptedNums)
# %%
k = len(nums)
i = 0
while val in nums:
    if nums[i] == val:
        del nums[i]
        k -= 1
        i = i
    else:
        pass
        i += 1
print(nums)
k
# %%
