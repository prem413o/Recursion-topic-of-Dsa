#binary search by recurasion
def binarysearch(arr,target,start,end):
    
    mid=(start + end)//2

    if(start> end):
        return -1

    if(arr[mid]==target):
        return mid

    elif(arr[mid]<target):
            
        return binarysearch(arr,target,mid+1,end)
    else:
        return binarysearch(arr,target,start,mid-1)
        
    


arr=[-3,4,5,9,23,56,89,99]
target=int(input("Enter your target: "))
result=binarysearch(arr,target,0,len(arr)-1)



if(result!=-1):
    print(f"the element found in index {result}")
else:
    print("the element not found")
