
public class BinarySearch {
    public static void main(String[] args) {
        
    }

    public int binarySearch(int[] arr, int target, int right, int left) {
        
            int middle = (left + right) / 2;

            if(left > right) {
                return -1;
            }

            if(arr[middle] == target) {
                return middle;
            }
            
            if(arr[middle] < target) {
                return binarySearch(arr, target, right, middle+1);
            }

            if(arr[middle] > target) {
                return binarySearch(arr, target, middle - 1, left);
            }
    }
}
