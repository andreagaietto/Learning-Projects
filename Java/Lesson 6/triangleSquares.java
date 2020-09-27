import java.util.Scanner;

public class triangleSquares {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //create scanner class and get user input
        System.out.print("Enter a number between 1 and 9: ");
        int n = input.nextInt();

        for (int i = 1; i <= n; i++) { //controls number of rows in the first block
            for (int column = n; column >= 1;column--) { //controls number of columns in each row
                if (column <= i) { //decides if a blank square or a number should be printed
                    System.out.printf("%3d", (column * column)); //prints the square, adds extra spaces to buffer to 3 as needed
                }
                else {
                    System.out.print("   ");
                }
            }
            System.out.println();
        }
        for (int k = (n-1); k >= 1; k--) {//controls number of rows in 2nd block
            for (int columnTwo = n; columnTwo >= 1; columnTwo--) {//controls number of columns in each row
                if (columnTwo > k) {//decides if a blank square or a number should be printed
                    System.out.print("   ");
                }
                else {
                    System.out.printf("%3d", (columnTwo * columnTwo));//prints the square, adds extra spaces to buffer to 3 as needed
                }
            }
        System.out.println();
        }
    }
}