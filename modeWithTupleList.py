# -*- coding: cp1254 -*-
def my_mode_with_list(my_hist_list):
 frequency_max=-1 # mode de�eri, d�ng�de kar��la�t�r�lacak haf�za ama�l� de�er
 mode=-1
 for item,frequency in my_hist_list:
 print(item,frequency)
 if frequency>frequency_max:
 frequency_max=frequency
 mode=item
 return mode,frequency_max
