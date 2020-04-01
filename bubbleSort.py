# -*- coding: cp1254 -*-
def my_bubble_sort(my_list):
 n=len(my_list)
 #print(my_list)
 for i in range(n-1,-1,-1):
 for j in range(0,i):
 if not(my_list[j]<my_list[j+1]):
 # print("swap işlemi")
 temp=my_list[j]
 my_list[j]=my_list[j+1]
 my_list[j+1]=temp
 return my_list
