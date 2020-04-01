# -*- coding: cp1254 -*-
def my_linear_search(my_list,item_search):
 found=(-1,-1) # default, eğer listede yoksa
 n=len(my_list)
 for indis in range(n):
 if my_list[indis]==item_search:
 found=(my_list[indis],indis) # listede bulundu, return bulunn sayı, indisi
 # break, uncomment for last found
 return found
