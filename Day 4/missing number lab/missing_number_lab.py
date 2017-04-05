def find_missing(array1, array2):
    if array1 == [] and array2 == []:
        return 0
    elif array1 == array2:
        return 0
    else:
        ans = list(set(array1) ^ set(array2))
        ans = ans[0]
        return ans

__author__ = 'Justin M'
