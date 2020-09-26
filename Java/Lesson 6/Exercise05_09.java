import java.util.Scanner;

public class Exercise05_09 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String firstName = " ";
        int firstGrade = 0;
        String secondName = " ";
        int secondGrade = 0;

        System.out.print("Enter the number of students: ");
        int numberStudents = input.nextInt();
        for (int i = 1; i <= numberStudents; i++) {
            System.out.print("Enter a student name: ");
            String name = input.next();
            System.out.print("Enter a student score: ");
            int grade = input.nextInt();
            if (grade > firstGrade) {
                secondName = firstName;
                secondGrade = firstGrade;
                firstName = name;
                firstGrade = grade;
            }
            else if ((grade > secondGrade) && (grade < firstGrade)) {
                secondName = name;
                secondGrade = grade;
            }
        }
        System.out.println("Top two students: ");
        System.out.print(firstName + "'s score is " + firstGrade + "\n");
        System.out.print(secondName + "'s score is " + secondGrade);

    }
}