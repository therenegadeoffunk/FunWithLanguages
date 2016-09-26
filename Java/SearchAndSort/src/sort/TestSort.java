package sort;
import java.util.*;

public class TestSort {

	public static void main(String[] args) {
		int[] arr = {5,8,3,7,1,2};
		sort.Sort.linearSearch(arr, 3);
		sort.Sort.linearSearch(arr, 2000);
		int[] sortedArr = {1,2,3,4,5,6,7,8,9,10};
		sort.Sort.binarySearch(sortedArr, 6);
		sort.Sort.binarySearch(sortedArr, 37);
	}
}