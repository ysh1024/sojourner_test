import re

def sum_number(num_str):
    sum_num = 0
    for a in num_str:
        sum_num += int(a)

    return str(sum_num)
