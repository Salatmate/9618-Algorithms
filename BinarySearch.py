arr = [1,3,5,7,9]

def BinarySearch(ele):
    global arr
    #requires array to be sorted
    lower_bound = 0
    upper_bound = len(arr)
    while lower_bound <= upper_bound:
        mid = (upper_bound+lower_bound)//2
        if arr[mid] == ele:
            return True
        elif arr[mid] < ele:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1

    #Time complexity O(log n)
    #Best case O(1)
    #Worst case O(log2 n)

    #Only condition for use of binary search is array must be sorted
    #Performance of binary search increases logarithmically as number of elements increases