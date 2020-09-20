import java.util.Scanner;
 public class WaterUsage {
     public static void main(String[] args) {

         Scanner input = new Scanner(System.in);

         double total = 0;

         System.out.print("Enter R for residential customer or B for business customer: ");
         String customerType = input.next();

         System.out.print("How many gallons of water were used? ");
         int gallons = input.nextInt();

         if (customerType.equals("R")) {
             if (gallons > 6000) {
                 total = ((6000 * .005) + ((gallons - 6000) * .007));
                 }
             else {
                 total = gallons * .005;
             }
         }
         else {
             if (gallons > 8000) {
                 total = ((8000 * .006) + ((gallons - 8000) * .008));
             }
             else {
                 total = gallons * .006;
             }
         }
         System.out.printf("Please pay this amount %.2f", total);
     }
 }