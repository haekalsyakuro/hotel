package pemrogramandasar;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class sort {
    public static void main(String[] args) throws Exception{
        ArrayList<Integer> arrNilai = new ArrayList<Integer>();
        Scanner sc = new Scanner (System.in);
        String[] nilai = {"A", "B", "C"};
        
        try {
            System.out.print("Masukkan Tiga Buah Nilai\n");
            
            for (String n : nilai){
                System.out.print("Nilai " + n + " : " );
                if(sc.hasNextInt()== true){
                    int inputNilai = sc.nextInt();
                    arrNilai.add(inputNilai);
                }else{
                    System.out.print("Harus Integer : ");
                    System.exit(0);
                }
            }
            
            showSortResult(bubbleSort("Ascending", arrNilai), "Ascending");
            System.out.print("\n");
            showSortResult(bubbleSort("Descending", arrNilai), "Descending");
            
            System.out.print("\n");
            System.out.print("Nilai MAX : " + Collections.max(arrNilai));
            System.out.print("\n");
            System.out.print("Nilai MIN : " + Collections.min(arrNilai));
            System.out.print("\n");
            
            System.out.print("Nilai RATA RATA : " + average(arrNilai));
        } catch (Exception e){
            System.out.print(e);
            sc.close();
            System.exit(0);
        } finally {
            sc.close();
            System.exit(0);
        }
    }
    
    public static void showSortResult(ArrayList<Integer> arrNilai, String sortName) {
        System.out.print("Urutkan Nilai " + sortName + " : ");
        for (int i = 0; i < arrNilai.size(); i++){
            System.out.print(arrNilai.get(i) + " ");
        }
    }
    
    public static ArrayList<Integer> bubbleSort(String order, ArrayList<Integer> arrNilai) {
        int temp;
        switch (order){
            case "Ascending":
            for (int i = 0; i <arrNilai.size(); i++){
                for (int j = i + 1; j < arrNilai.size(); j++){
                    if (arrNilai.get(i) > arrNilai.get(j)){
                        temp = arrNilai.get(i);
                        arrNilai.set(i, arrNilai.get(j));
                        arrNilai.set(j, temp);                    
                    }
                }
            }
            break;
            case "Descending":
                for (int i=0; i  < arrNilai.size(); i++){
                    for (int j = i + 1; j <arrNilai.size(); j++) {
                        if (arrNilai.get(i) < arrNilai.get(j)){
                            temp = arrNilai.get(i);
                            arrNilai.set(i, arrNilai.get(j));
                            arrNilai.set(j, temp);
                        }
                    }
                }
                break;
        }
        return arrNilai;
    }
    public static Integer average(ArrayList<Integer> arrNilai){
        int total = 0;
        for (int i = 0; i <arrNilai.size(); i++){
        total += arrNilai.get(i);
    }
        return Math.round((Integer) total / arrNilai.size());
    }
    // 
}