import java.util.Scanner;

public class Game {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int finalPosition = 0;
        int userInput = -1;

        while (userInput != 0) {
            System.out.println("You are now at position " + finalPosition);
            System.out.println("What do you want to do?");
            System.out.println("0 to exit");
            System.out.println("1 to move 1 space,");
            System.out.println("2 to roll");
            userInput = input.nextInt();
            if (userInput == 0) {
                break;
            }
            else if (userInput == 1) {
                finalPosition = Utils.move(finalPosition, 1);
            }
            else if (userInput == 2) {
                int rollValue = Utils.roll() + Utils.roll();
                int newPosition = Utils.move(finalPosition, rollValue);
                int numMoves = newPosition - finalPosition;
                finalPosition = newPosition;
                System.out.println("You rolled " + rollValue + " and moved " + numMoves + " spaces");
            }
            if (finalPosition == 100) {
                System.out.println("You won");
                System.out.println("Bye");
                break;
            }
        }

    }
}