import java.util.Scanner;

public class Exercise03_11 {
    public static void main(String[] args) {

        int days = 0; // declare days as int prior to later use
        String monthName;

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a month in the year (e.g., 1 for Jan) ");
        int month = input.nextInt();

        System.out.print("Enter a year: ");
        int year = input.nextInt();

        if (month == 2) {   //if month is February, check to see if year is leap year and assign days
            monthName = "February";
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                days = 29;
            }
            else {
                days = 28;
            }
        }
        else if (month == 1) {
            days = 31;
            monthName = "January";
        }
        else if (month == 3) {
            days = 31;
            monthName = "March";
        }
        else if (month == 4) {
            days = 30;
            monthName = "April";
        }
        else if (month == 5) {
            days = 31;
            monthName = "May";
        }
        else if (month == 6) {
            days = 30;
            monthName = "June";
        }
        else if (month == 7) {
            days = 31;
            monthName = "July";
        }
        else if (month == 8) {
            days = 31;
            monthName = "August";
        }
        else if (month == 9) {
            days = 30;
            monthName = "September";
        }
        else if (month == 10) {
            days = 31;
            monthName = "October";
        }
        else if (month == 11) {
            days = 30;
            monthName = "November";
        }
        else {
            days = 31;
            monthName = "December";
        }
        System.out.print(monthName + " " + year + " has " + days + " days");
    }
}