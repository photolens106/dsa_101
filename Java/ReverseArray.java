public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        System.out.println("Original Array: ");
        printArray(arr);

        reverseArray(arr);

        System.out.println("Reversed Array: ");
        printArray(arr);
    }

    public static void printArray(int[] arr){
        for (int num: arr){
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void reverseArray(int[] arr){
        int left=0, right=arr.length-1;
        while (left < right){
            // Swap Elements
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            // Move pointers
            left++;
            right--;
        }
    }
}
