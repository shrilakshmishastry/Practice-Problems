# quick sort 

def quickSort(arr,low,high):

    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)



def partition(arr,low,high):
    #code for partition

    p = arr[low]
    i,j =low+1,high
    print(j)
    while(low < high):
        while(i<high and arr[i]<=p  ):
            i = i+1

        while(arr[j]>p)    :
            j=j-1
        if(i<j)    :
            arr[i],arr[j] = arr[j],arr[i]

    print(1,arr)
    # arr[i],arr[j] = arr[j],arr[i]
    print(2,arr)
    arr[low],arr[j] = arr[j],arr[low]
    print(3,arr)
    return j

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())

    for i in range(0,t):
        n = int(input())
        arr = map(int,input().strip().split())
        arr = list(arr)
        quickSort(arr,0,n-1)
        for i in range(0,n):
            print(arr[i],end = " ")
