import java.util.Scanner;

public class Exercise04_13 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a letter: ");
        String userSelection = input.next();

        char charSelection = userSelection.charAt(0);

        if ((charSelection >= 65 && charSelection <= 90) || (charSelection >= 97 && charSelection <= 122)) {
            if ("AEIOUaeiou".contains(userSelection)) {
                System.out.println(userSelection + " is a vowel");
            }
            else {
                System.out.println(userSelection + " is a consonant");
            }
        }
        else {
            System.out.println(userSelection + " is an invalid input");
        }

    }
}