def subset(arr,ans,i):

    if i==len(arr):
       print(ans)
       return 
     

    ans.append(arr[i]) #include of element
    subset(arr,ans,i+1)

    ans.pop()
    subset(arr,ans,i+1)

arr=[1,2,3]
ans=[]
subset(arr,ans,0)