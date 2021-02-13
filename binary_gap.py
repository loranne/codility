def solution(N):
    """Takes in int N, returns longest binary gap"""

    binary_n = bin(N)[2:]

    gaps = binary_n.split("1")

    # if binary ends with a zero, like bin(32), should return zero
    # but only need to discount the one before it!
    if gaps[-1] != "":
        return 0

    if gaps[-1] != "":
        gaps[len(gaps) - 2] = 0
        print(gaps[len(gaps) - 2])

    count = 0

    for x in gaps:
        if len(x) > count:
            count = len(x)
    
    return count

print(solution(32))
print(solution())