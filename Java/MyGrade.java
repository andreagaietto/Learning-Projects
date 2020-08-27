import java.util.Scanner;

public class MyGrade {
    public static void main(String[] args) {

        double labsWeight = 20.0;
        double readingWeight = 15.0;
        double revelWeight = 15.0;
        double midtermWeight = 15.0;
        double projectWeight = 20.0;
        double finalWeight = 15.0;

        Scanner input = new Scanner(System.in);
        System.out.println("Enter Labs average in percent: ");
        int labs = input.nextInt();
        System.out.println("Enter Reading Quizzes average in percent: ");
        int reading = input.nextInt();
        System.out.println("Enter REVEL average in percent: ");
        int revel = input.nextInt();
        System.out.println("Enter Midterm average in percent: ");
        int midterm = input.nextInt();
        System.out.println("Enter Project average in percent: ");
        int project = input.nextInt();
        System.out.println("Enter Final average in percent: ");
        int finalExam = input.nextInt();
        double average = (int) ((labs * labsWeight) + (reading * readingWeight) + (revel * revelWeight) + (midterm * midtermWeight) +
                (project * projectWeight) + (finalExam * finalWeight)) / 100.0;
        System.out.println("Your average is " + average);


    }

}