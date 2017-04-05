def find_max_min(my_list):
    max_no = max(my_list)
    min_no = min(my_list)

    # check to see if max_no and min_no are equal
    if max_no == min_no:
        new_list = []
        new_list.append(len(my_list))
        return new_list

    # else min_no and max_no in an array
    else:
        return [min_no, max_no]
__author__ = 'Justin M'
