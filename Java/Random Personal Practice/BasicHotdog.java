import java.util.Scanner;
public class BasicHotdog {
    public static void main(String[] args) {

        final double HOTDOG_PRICE = 2.50;
        final double CHIP_PRICE = 1.50;
        final double SODA_PRICE = 1.25;

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of hotdogs: ");
        int hotdogs = input.nextInt();
        System.out.print("Enter the number of chips: ");
        int chips = input.nextInt();
        System.out.print("Enter the number of sodas: ");
        int soda = input.nextInt();

        double total = (hotdogs * HOTDOG_PRICE) + (soda * SODA_PRICE) + (chips * CHIP_PRICE);

        System.out.printf("Price is %.2f", total);
    }
}