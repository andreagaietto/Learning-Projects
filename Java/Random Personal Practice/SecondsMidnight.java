import java.util.Scanner;

public class SecondsMidnight {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int midnight_seconds = 0;

        System.out.print("Enter hour: ");
        int hour = input.nextInt();
        System.out.print("Enter minute: ");
        int minute = input.nextInt();
        System.out.print("Enter second: ");
        int second = input.nextInt();
        System.out.print("Enter AM or PM: ");
        String time = input.next();


        if (hour == 12 && time.equals("AM")) {
            midnight_seconds = (60 * minute) + second;
        }
        else if (time.equals("AM") || (time.equals("PM") && hour == 12)) {
            midnight_seconds = (hour * 3600) + (minute * 60) + second;
        }
        else {
            midnight_seconds = ((hour * 3600) + (minute * 60) + second) + 43200;
        }
        System.out.println("Seconds since midnight: " + midnight_seconds);
    }
}