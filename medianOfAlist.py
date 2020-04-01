def my_median(my_list):
 my_list_2=bubble_sort(my_list)
 #print(my_list_2)
 n=len(my_list_2)
 if n%2==1:
 middle=int(n/2)+1
 median=my_list_2[middle]
 #print(median)
 else:
 middle_1=my_list_2[int(n/2)]
 middle_2=my_list_2[int(n/2)+1]
 median=(middle_1+middle_2)/2
 #print (median)

 return median
