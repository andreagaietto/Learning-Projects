import java.util.Scanner;
public class Exercise02_05{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double gratuity;
        double total;

        System.out.println("Enter the subtotal and a gratuity rate: ");
        double subtotal = input.nextDouble();
        double gratuityRate = input.nextDouble();

        gratuity = (gratuityRate / 100) * subtotal;
        total = subtotal + gratuity;

        System.out.println("The gratuity is $" + gratuity + " and total is $" + total);


    }
}