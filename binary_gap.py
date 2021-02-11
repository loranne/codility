def solution(N):
    """Takes in int N, returns longest binary gap"""

    binary_n = bin(N)[2:]

    gaps = binary_n.split("1")

    if gaps[-1] != "":
        return 0

    count = 0

    for x in gaps:
        if len(x) > count:
            count = len(x)
    
    return count