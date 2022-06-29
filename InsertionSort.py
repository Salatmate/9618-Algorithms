arr = [9,3,5,7,1,8,2,6,4]

def InsertionSort():
    global arr
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    #Time complexity O(n^2)
    #Best case O(1)
    #Worst case O(n^2/2)