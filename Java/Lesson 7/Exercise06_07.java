import java.util.Scanner;

public class Exercise06_07 {
    //futureInvestmentValue =investmentAmount × (1 + annual/12)^numberOfYears*12
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double investmentAmount;
        double annualInterestRate;
        double monthlyInterestRate;

        System.out.print("The amount invested: ");
        investmentAmount = input.nextDouble();

        System.out.print("Annual interest rate: ");
        annualInterestRate = input.nextDouble();
        monthlyInterestRate = annualInterestRate / 1200;

        for (int i = 1; i <= 30; i++) {
            double futureValue = futureInvestmentValue(investmentAmount, monthlyInterestRate, i);
            System.out.printf("%d %.2f \n", i, futureValue);
        }

    }



    public static double futureInvestmentValue(double investmentAmount, double monthlyInterestRate, int years) {
        double investmentValue = investmentAmount * (Math.pow((1 + monthlyInterestRate), (years * 12)));
        return investmentValue;
    }
}