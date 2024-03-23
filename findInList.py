def b_srt(lst):  
    for i in range(0,len(lst)-1):  
        for j in range(len(lst)-1):  
            if(lst[j]>lst[j+1]):  
                temp = lst[j]  
                lst[j] = lst[j+1]  
                lst[j+1] = temp  
    return lst  
  
lst = []  
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    a = int(input())
    lst.append(a) 

print("The unsorted list is: ", lst)  
print("The sorted list is: ", b_srt(lst))