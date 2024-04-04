def binarySearch (Arr, L, R, X):
    if R >= L:
        mid = L + (R - L)//2
        if Arr[mid] == X:
            return mid
        elif Arr[mid] > X:
            return binarySearch(Arr, L, mid-1, X)
        else:
            return binarySearch(Arr, mid+1, R, X)
    else:
        return -1

#calling the function
data = [10,20,30,40,50,60,70,80,90,100]
key = 90
index = binarySearch(data,0,len(data)-1,key)
if(index!=-1):
  print('Found at position :',index+1)
else:
  print('Not found')