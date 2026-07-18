def solution(n):
    array = [0, 1]
    for x in range(2, n + 1):

        next = (array[x-1] + array[x-2]) % 1234567
        array.append(next)

    return array[n]