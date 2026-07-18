def solution(my_string, s, e):
    
    cut_line_A = my_string[:s]
    
    reversed_part = my_string[s:e+1][::-1]
    
    cut_line_B = my_string[e+1:]
    
    return cut_line_A  + reversed_part + cut_line_B