def search(arr, n):
    for i in range(0, len(arr)): 
       if arr[i]==n: 
           return True
    return False


arr = [5,4,3,6,7,8,9,1]
present = search(arr, 9)
if present==True:
    print("P")
else:
    print("N")