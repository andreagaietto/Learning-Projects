import java.util.Scanner;

public class Exercise06_23 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String str = input.nextLine();

        System.out.print("Enter a character: ");
        char a = input.next().charAt(0);

        int totalCount = count(str, a);

        System.out.print("The number of occurrences of " + a + " in " + str + " is " + totalCount);
    }

    public static int count(String str, char a) {
        int isEqual = 0;
        // s.equals(s1) if string is equal to s1
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == a) {
                isEqual += 1;
            }
        }
        return isEqual;
    }
}