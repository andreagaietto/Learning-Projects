import java.util.Scanner;

public class Exercise03_21 {
    public static void main(String[] args) {

        int k;
        int j;
        String weekDay;
        int h;

        Scanner input = new Scanner(System.in);

        System.out.print("Enter year: ");
        int year = input.nextInt();

        System.out.print("Enter month: ");
        int m = input.nextInt();

        System.out.print("Enter the day of the month: ");
        int q = input.nextInt();

        if (m == 1) {
            m = 13;
            year -= 1;
        }
        else if (m == 2) {
            m = 14;
            year -= 1;
        }

        k = year % 100;
        j = (year / 100);

        h = (q + (26 * (m + 1)/10) + k + (k/4) + (j/4) + (5 * j)) % 7;
        // h = (q + ((26 * (m + 1))/10) + k + (k/4) + (j/4) + (5 * j)) % 7;
        if (h == 0) {
            weekDay = "Saturday";
        }
        else if (h == 1) {
            weekDay = "Sunday";
        }
        else if (h == 2) {
            weekDay = "Monday";
        }
        else if (h == 3) {
            weekDay = "Tuesday";
        }
        else if (h == 4) {
            weekDay = "Wednesday";
        }
        else if (h == 5) {
            weekDay = "Thursday";
        }
        else {
            weekDay = "Friday";
        }

        System.out.print("Day of the week is " + weekDay);




    }
}

