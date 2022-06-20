#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nouv_list = []
    for a in range(0, list_length):
        try:
            dev = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            dev =  0
        except ZeroDivisionError:
            print("division by 0")
            dev = 0
        except IndexError:
            print("out of range")
            dev = 0
        finally:
            nouv_list.append(dev)
    return(nouv_list)
