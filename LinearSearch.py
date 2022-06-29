arr = [1,3,5,7,9]

def LinearSearch(ele):
    global arr
    for i in range(len(arr)):
        if arr[i] == ele:
            return True
    return False

    #O(n) time complexity
    #Best case O(1)
    #Worst case O(n)