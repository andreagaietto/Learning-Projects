import java.util.Scanner;
public class Exercise02_07{
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of minutes: ");
        long minutes = input.nextLong();
        long hours = minutes / 60;
        long days = hours / 24;
        long years = days / 365;
        long remainingDays = days % 365;

        System.out.println(minutes + " minutes is approximately " + years + " years and " + remainingDays + " days");

    }

}

