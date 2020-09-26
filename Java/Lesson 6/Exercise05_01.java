import java.util.Scanner;

public class Exercise05_01{
    public static void main(String[] args) {
        int userNumber;
        int positives = 0;
        int negatives = 0;
        int total = 0;
        double average = 0.0;

        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer, the input ends if it is 0: ");
        userNumber = input.nextInt();
        while (userNumber != 0){
            if (userNumber > 0) {
                positives += 1;
            }
            else if (userNumber < 0) {
                negatives += 1;
            }
            total += userNumber;
            userNumber = input.nextInt();
        }
        if ((positives == 0) && (negatives == 0)){
            System.out.println("No numbers are entered except 0");
        }
        else {
            System.out.println("The number of positives is " + positives);
            System.out.println("The number of negatives is " + negatives);
            System.out.println("The total is " + total);
            average = ((double)total/ (positives + negatives));
            System.out.println("The average is " + average);
        }

    }
}