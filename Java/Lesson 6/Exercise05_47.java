import java.util.Scanner;

public class Exercise05_47 {
    public static void main(String[] args) {

        int total = 0;
        int tempNumber = 0;
        int lastNumber = 0;
        String tempString = " ";

        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first 12 digits of an ISBN-13 as a string: ");
        String userInput = input.next();

        if (userInput.length() == 12) {
            for (int i = 0; i < 12; i++){
                tempString = userInput.charAt(i) + "";
                tempNumber = Integer.parseInt(tempString);
                if ((i % 2) == 0) {
                    total += (tempNumber * 3);
                }
                else {
                    total += tempNumber;
                }

            }
            lastNumber = (10 - (total) % 10);
            if (lastNumber == 10){
                lastNumber = 0;
            }
            System.out.print("The ISBN-13 number is " + userInput + lastNumber);
        }
        else {
            System.out.print(userInput + " is an invalid input.");
        }
    }
}