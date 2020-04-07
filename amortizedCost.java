/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package amortizedcost;

import java.util.Arrays;

/**
 *
 * @author Uğur
 */
public class AmortizedCost {

    public static void main(String[] args) {
        
        DynamicArray dynamicArray = new DynamicArray();
        
        dynamicArray.append(1);
        dynamicArray.append(2);
        dynamicArray.append(3);
        dynamicArray.append(4);
        dynamicArray.append(5);
        dynamicArray.remove();
        dynamicArray.remove();
        dynamicArray.remove();
        dynamicArray.remove();
        dynamicArray.remove();

        System.out.println(dynamicArray);

    }

}

class DynamicArray {

    private int capacity = 1;
    private int array[] = new int[capacity];
    private int n = 0;
    
    
    //Dizinin sonuna eleman ekler, karmaşıklığı O(n)
    public void append(int items) {

        if (n == capacity) {

            System.out.println("Dizi boyutu ikiye katlandı....");
            resize();//O(n)
        }
        System.out.println("Boyut: " + (n + 1) + ", Kapasite: " + capacity);
        array[n] = items;
        n++;
    }
    
    //Dizinin son elemanını siler, karmaşıklığı O(n)+O(n) = O(n)
    public void remove() {
        
        //O(n)
        for (int i = array.length - 1; i < n - 1; i--) {
            array[i] = array[i - 1];
        }

        System.out.println("Boyut: " + (n) + ", Kapasite: " + capacity);
        
        trimSize();//O(n)
        n--;

    }

    //Dizi boyutu yetersiz kaldığında kapasiteyi iki katına çıkartır, karmaşıklık O(n)
    public void resize() {
        int temp[] = new int[capacity * 2];

        // dizi kopyalama metodu, bu metot karmaşıklığı O(n) 
        for (int i = 0; i < capacity; i++) {
            temp[i] = array[i];
        }
        array = temp;
        capacity *= 2;
    }

    //diziden eleman silindiği zaman kapasiteyi azaltır, karmaşıklık O(n)
    public void trimSize() {
        int temp[] = new int[n];
        
        //O(n)
        for (int i = 0; i < n; i++) {
            temp[i] = array[i];
        }
        array = temp;
        capacity = array.length;
    }

    @Override
    public String toString() {
        return "DynamicArray{" + "dizi kapasitesi= " + capacity + ", dizi elemanları= " + Arrays.toString(array) + ", dizi boyutu=" + n + '}';
    }

}
