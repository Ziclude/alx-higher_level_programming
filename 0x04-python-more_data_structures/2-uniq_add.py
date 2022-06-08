#!/usr/bin/python3
def uniq_add(my_list=[]):
    answer = 0
    for a in set(my_list):
        answer += a
    return answer
