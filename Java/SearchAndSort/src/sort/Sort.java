package sort;
import java.util.*;

// We're using void methods that just print out to console since
// this is just for instructional purposes

public class Sort {

	public static void linearSearch(int[] arr, int key){
		for (int i=0; i < arr.length; i++){
			if (arr[i] == key){
				System.out.println("We found the key " + key);
				return;
			}
		}
		System.out.println("Kill yourself");
	}
	
	//Broken. Need to fix.
	
	public static void binarySearch(int[] L, int k){
		int low = 0;
		int high = L.length-1;
		int mid = high/2;
		while (low <= high) {
			if (k == L[mid]){
				System.out.println("We did it, Reddit!");
				return;
			}
			else if (k > L[mid]){
				low = mid;
			}
			else if (k < L[mid]){
				high = mid;
			}
			int newmid = (low + high)/2;
			if (mid == newmid){
				System.out.println("We're done here.");
				return;
			}
			mid = newmid;
		}
		System.out.println("IT'S HAPPENING");
		return;
	}
}