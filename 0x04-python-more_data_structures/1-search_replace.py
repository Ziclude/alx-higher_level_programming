#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nouv_list = my_list[:]
    for a in range(len(nouv_list)):
        if nouv_list[a] == search:
            nouv_list[a] = replace
    return nouv_list
