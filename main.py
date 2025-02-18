"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)
# returns the element in the fibbonacci sequence at index x. So foo(3) would return the fourth element in the sequence at index 3.

def longest_run(mylist, key):
    count = 0
    longest = 0
    for num in mylist:
        if num == key:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 0
    return max(count,longest)

# Both the work and span of this implementation are O(n), as the amount of comparisons is proportional to the input size so the work is O(n)
# No parallelism is possible because each comparison is dependent on the previous values, making the algorithm sequential. So the span is O(n)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)

def combine(left,right):
    is_entire_range = left.is_entire_range and right.is_entire_range
    
    
def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)
    else:
        left = longest_run_recursive(mylist[:len(mylist)//2], key) 
        right = longest_run_recursive(mylist[len(mylist)//2:], key)
        combine_results(left,right)

def combine_results(result1, result2):
    if result1.is_entire_range and result2.is_entire_range:
        total = result1.longest_size + result2.longest_size
        return Result(total, total, total, True)
    else:
        left_size = result1.left_size
        if result1.is_entire_range:  
            left_size += result2.left_size

        right_size = result2.right_size
        if result2.is_entire_range: 
            right_size += result1.right_size

        overlap = result1.right_size + result2.left_size

        return Result(
            left_size,
            right_size,
            max(overlap, result1.longest_size, result2.longest_size),
            False
        )
# 3d) 
#    W(n) = 2W(n/2) + 1    
#    S(n) = O(log(n))

# 3e)
#    Work would stay the same
#    New S(n/2) + 1






