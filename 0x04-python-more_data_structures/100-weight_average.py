#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    aver = 0
    sz = 0
    for tp in my_list:
        aver += (tp[0] * tp[1])
        sz += tp[1]
    return (aver / sz)
