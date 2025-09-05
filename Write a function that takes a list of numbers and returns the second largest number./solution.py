def second_largest(nums):
    largest = second = float('-inf')
    
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n
    
    return second if second != float('-inf') else None