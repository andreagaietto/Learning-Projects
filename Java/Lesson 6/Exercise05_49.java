import java.util.Scanner;

public class Exercise05_49 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int vowels = 0;
        int consonants = 0;
        System.out.print("Enter a string: ");
        String userInput = input.nextLine().toUpperCase();
        System.out.println(userInput);
        for (int i = 0; i < userInput.length(); i++) {
            String myChar = userInput.charAt(i) + "";
            if ("AEIOU".contains(myChar)) {
                vowels += 1;
            }
            else if (userInput.charAt(i) != 32) {
                consonants += 1;
            }
        }
        System.out.println("The number of vowels is " + vowels);
        System.out.println("The number of consonants is " + consonants);

    }
}
