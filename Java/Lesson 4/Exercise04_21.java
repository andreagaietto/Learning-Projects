import java.util.Scanner;
public class Exercise04_21 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a SSN: ");

        String socialNumber = input.next();



        boolean isCorrect = socialNumber.length() == 11 && Character.isDigit(socialNumber.charAt(0)) && Character.isDigit(socialNumber.charAt(1)) && Character.isDigit(socialNumber.charAt(2)) && socialNumber.charAt(3) == '-' && Character.isDigit(socialNumber.charAt(4)) && Character.isDigit(socialNumber.charAt(5)) && socialNumber.charAt(6) == '-' && Character.isDigit(socialNumber.charAt(7)) && Character.isDigit(socialNumber.charAt(8)) && Character.isDigit(socialNumber.charAt(9)) && Character.isDigit(socialNumber.charAt(10));

        if (isCorrect) {
            System.out.println(socialNumber + " is a valid social security number");
        }
        else {
            System.out.println(socialNumber + " is an invalid social security number");
        }

    }
}