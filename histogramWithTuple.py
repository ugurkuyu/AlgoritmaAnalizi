# -*- coding: cp1254 -*-
def my_frequency_with_list_of_tuples(list_1):
 frequency_list=[]
 for i in range(len(list_1)):
 s=False
 for j in range(len(frequency_list)):
 if (list_1[i]==frequency_list[j][0]):
 frequency_list[j][1]=frequency_list[j][1]+1
 s=True
 if(s==False):
 frequency_list.append([list_1[i],1])
 return frequency_list
