import java.util.Scanner;

public class Exercise05_17 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("enter the number of lines: ");
        int numLines = input.nextInt();

        for (int rows = 1; rows <= numLines; rows++) {
            int numPrint = rows;
            for (int cols = 1; cols <= ((numLines * 2) - 1); cols ++) {
                if ((cols <= (numLines - rows)) || (cols >= (numLines + rows))) {
                    System.out.print("   ");
                }
                else {
                    if (cols < numLines) {
                        System.out.printf("%3d", numPrint);
                        numPrint --;
                    }
                    else {
                        System.out.printf("%3d", numPrint);
                        numPrint ++;

                    }
                }
            }
            System.out.println();
        }
    }
}
