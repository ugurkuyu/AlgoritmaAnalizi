# -*- coding: cp1254 -*-
import random
def getModeMedian():
    list_1=[]
    n=random.randint(3, 10)#dizi uzunluðu
    r_min=-4#dizinin içinde yer alabilecek en küçük deðer
    r_max=4#dizinin içinde yer alabilecek en büyük deðer
    
    #Diziye rastgele deðer atanmasý
    #karmaþýklýk O(n)
    for i in range(n):
        list_1.append(random.randint(r_min,r_max))
    print ("liste", list_1)
    
    
    #Dizinin histogram deðerinin hesaplanmasý
    #Karmaþýklýk O(n*n)
    histogram_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(histogram_list)):
            if (list_1[i]==histogram_list[j][0]):
                 histogram_list[j][1]=histogram_list[j][1]+1
                 s=True
        if(s==False):
            histogram_list.append([list_1[i],1])
    
    print("histogram_list", histogram_list)
    
    #Dizinin mod hesabýnýn yapýlmasý
    #Karmaþýklýk O(n)
    frekans_max = -1
    mod = -1
    for item, frekans in histogram_list:
       print("item", item, "frekans", frekans)
       if(frekans > frekans_max):
           frekans_max = frekans
           mod = item
    print("mod", mod, "max_f", frekans_max)

    #Dizinin buble sort ile sýralanmasý
    #Karmaþýklýk O(n*n)
    m = len(list_1)
    for i in range(m-1, -1, -1):
        for j in range(0, i):
            if not(list_1[j] < list_1[j+1]):
                temp = list_1[j]
                list_1[j] = list_1[j+1]
                list_1[j+1] = temp
    print(list_1)
    
    
    #Dizinin median hesabýnýn yapýlmasý
    #Yukarýda sýralanan diziyi kullanacaðýmýz için karmaþýklýkk O(n)
    
    if(m % 2 == 1):
        ortanca = int(m/2) 
        median = list_1[ortanca]
        print("Median = ", median)
    else:
        ort_1 = list_1[int(m/2)]
        ort_2 = list_1[int(m/2) - 1]
        median = (ort_1 + ort_2) / 2
        print("Median = ", median)
    
    return mod, median   
