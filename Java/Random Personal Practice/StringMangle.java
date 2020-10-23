import java.util.Scanner;


public class StringMangle {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        String clipboard = "";

        System.out.println("Enter a string");
        String currentString = input.next();

        System.out.println("The current string is");
        StringUtils.genGauge(currentString);

        System.out.println("Enter c to copy, x to cut, v to paste, q to quit");
        String userChoice = input.next();

        while (!userChoice.equals("q")) {
            if (userChoice.equals("c")) {
                System.out.println("Enter the starting position");
                int startPosition = input.nextInt();
                System.out.println("Enter one past the ending position");
                int onePastLastPosition = input.nextInt();
                clipboard = StringUtils.copy(currentString, startPosition, onePastLastPosition);
            }
            else if (userChoice.equals("x")) {
                System.out.println("Enter the starting position");
                int startPosition = input.nextInt();
                System.out.println("Enter one past the ending position");
                int onePastLastPosition = input.nextInt();
                currentString = StringUtils.cut(currentString, startPosition, onePastLastPosition);
            }
            else if (userChoice.equals("v")) {
                System.out.println("Enter the position the paste should come before");
                int insertBefore = input.nextInt();
                currentString = StringUtils.paste(currentString, insertBefore, clipboard);
            }
            System.out.println("The current string is");
            StringUtils.genGauge(currentString);
            System.out.println("The clipboard is \n" + clipboard + " and it has length of " + clipboard.length());
            System.out.println("\nEnter c to copy, x to cut, v to paste, q to quit");
            userChoice = input.next();
        }
    }
}