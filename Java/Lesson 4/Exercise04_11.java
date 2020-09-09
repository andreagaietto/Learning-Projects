import java.util.Scanner;

public class Exercise04_11 {
    public static void main(String[] args) {

        char charInput;

        Scanner input = new Scanner(System.in);
        System.out.print("Enter a decimal value (0 to 15): ");
        int userInput = input.nextInt();

        if (userInput < 0 || userInput > 15) {
            System.out.println(userInput + " is an invalid input");
        }
        else if (userInput <= 9) {
            System.out.println("The hex value is " + userInput);
        }
        else if (userInput >= 10 || userInput <= 15){
            charInput = (char)(userInput + 55);
            System.out.println("The hex value is " + charInput);

        }
    }
}