def solution(sequence, k):

    min_length = float('inf')
    answer = []
    
    left = 0
    current_sum = 0
    
    for right in range(len(sequence)):

        current_sum += sequence[right]
        
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1

        if current_sum == k:
            current_sum_length = right - left

            if current_sum_length < min_length:
                min_length = current_sum_length
                answer = [left, right]
                
    return answer