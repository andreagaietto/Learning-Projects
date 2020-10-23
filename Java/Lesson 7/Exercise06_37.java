import java.util.Scanner;

public class Exercise06_37 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int number = input.nextInt();

        System.out.print("Enter the width: ");
        int width =  input.nextInt();

        String formatted = format(number, width);

        System.out.print("The formatted number is " + formatted);


    }
    public static String format(int number, int width) {
        String formattedInt = number + " ";
        if (formattedInt.length() > width) {
            return formattedInt;
        }
        else {
            for (int i = formattedInt.length(); i <= width; i++) {
                formattedInt = "0" + formattedInt;
            }
            return formattedInt;
        }
    }
}