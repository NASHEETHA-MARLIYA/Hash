def finding_max_and_smax(arr):
    max_ele=arr[0]
    smax_ele=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_ele:
            smax_ele=max_ele
            max_ele=arr[i]
        elif arr[i]>smax_ele and arr[i]<max_ele:
            smax_ele=arr[i]
    return max_ele,smax_ele
arr=[123,543,345,654,876,678,987,234,98,45,765,34,765,34,6,8]
max_ele,smax_ele= finding_max_and_smax(arr)
print("The Largest Element is ",max_ele)
print("The Second Largest Element is ",smax_ele)
