def solution(A):
    # write your code in Python 3.6
    """Takes in array (list) of ints of len N, returns smallest int that does not appear in A"""
    
    small_int = 1
    
    sorted_a = sorted(A)
    
    for x in sorted_a:
        if x == small_int:
            small_int += 1
        elif x < small_int:
            pass
        else:
            break
    
    return small_int

# think about what to do if item in list is >, <, or = to small_int
# can eliminate set aspect
# if < small_int, ignore
# if == small_int, increment
# if > small_int, return small_int

    # small_int = 1


    # list_a = list(set_a)

    # positive_list = []

    # for i in list_a:
    #     if i > 0:
    #         positive_list.append(i)

    # sorted_list = sorted(positive_list)

    # for x in sorted_list:
    #     if x == small_int:
    #         small_int += 1
    #     else: 
    #         break
    
    # return small_int


print(solution([-1, -3]))
print(solution([2, 1, 4, 3, 6]))
print(solution([1]))
print(solution([1, 2, 0, 3, 4, 7, 8, 9, 10]))
print(solution([]))
