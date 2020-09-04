import java.util.Scanner; // import scanner

public class Weekend {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); //create new scanner object and obtain responses from user

        System.out.print("Are parents visiting? Enter 1 for yes, 2 for no: ");
        int parents = input.nextInt();

        System.out.print("Is the weather good? Enter 1 for yes, 2 for no: ");
        int weather = input.nextInt();

        System.out.print("Are you rich? Enter 1 for yes, 2 for no: ");
        int rich = input.nextInt();


        if (parents == 1) { // outer selection statement for parents == visiting. Only the weather matter when they visit
            if (weather == 1) { // check for the weather
                System.out.print("You should go to the cinema.");
            }
            else {
                System.out.print("You should stay in.");
            }
        }
        else if (parents == 2) { // outer selection statement for parents not visiting
            if (rich == 2) { //inner selection statements based on various factors
                System.out.print("You should stay in.");
            }
            else if (rich == 1 && weather == 1) {
                System.out.print("You should go shopping.");
            }
            else {
                System.out.print("You should go to the cinema.");
            }
        }
    }
}

