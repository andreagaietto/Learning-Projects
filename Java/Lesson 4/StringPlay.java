import java.util.Scanner;

public class StringPlay {
    public static void main(String[] args) {

        // declare variable types in advance
        String firstTwo;
        String lastFive;
        String switchedLetters;
        int firstE;
        int firstS;
        int stringLength;

        Scanner kybd = new Scanner(System.in);

        System.out.println("Enter a line of text: ");

        String aLine = kybd.nextLine(); //obtain a string from user

        stringLength = aLine.length(); //obtain length of aLine and assign to a variable for use

        if (stringLength < 7) { //check the the string is not too short
            System.out.println("The input is too short");
        }
        else {
            String trimmed = aLine.trim(); //trim any whitespace and return trimmed string
            if (stringLength > trimmed.length()) { //check lengths to see if any whitespace was removed
                System.out.println("The original String has leading or trailing whitespace.");
            }
            else {
                System.out.println("The original string has no leading or trailing whitespace.");
            }
            firstTwo = aLine.substring(0, 2); //obtain first two characters from string
            lastFive = aLine.substring((stringLength - 5));//obtain last 5 characters from string
            switchedLetters = (lastFive + aLine.substring(2, stringLength - 5)) + (firstTwo); //swap letters and store in variable. adding the last five with the trimmed middle, then tacking on first two on the end
            System.out.println("First 2 and last 5 chars swapped: " + switchedLetters); //print swapped string
            System.out.println("to upper case: " + aLine.toUpperCase()); //print in all caps
            if (stringLength % 2 != 0) { //check if the string has an even number of characters and print statement if odd number
                System.out.println("The line has an odd number of characters.");
            }
            else {
                System.out.println("The middle two characters are " + aLine.substring((stringLength / 2 - 1), (stringLength / 2 + 1))); //obtain and print middle two characters
            }
            System.out.println("compareTo lower case version: " + aLine.compareTo(aLine.toLowerCase())); //force lower case and compare
            System.out.println("Does the first half equal the last half? " + aLine.substring(0, stringLength / 2).equalsIgnoreCase(aLine.substring(stringLength / 2))); //check if both halves match, minus case
            firstE = aLine.toUpperCase().indexOf("E"); //check index of first occurrence of E, with all caps for ease
            firstS = aLine.toUpperCase().indexOf("S"); //check index of first occurrence of S, with all caps for ease
            if (firstE != -1 && firstS == -1) {// take the value of firstE out if firstE exists and firstS does not
                System.out.println("The input with first 'e' or 'E' or 's' or 'S' removed: " + aLine.substring(0, firstE) + aLine.substring(firstE + 1));
            }
            else if (firstS != -1 && firstE == -1) {//take the value of firstS out if firstS exists and firstE does not
                System.out.println("The input with first 'e' or 'E' or 's' or 'S' removed: " + aLine.substring(0, firstS) + aLine.substring(firstS + 1));
            }
            else if (firstE != -1 && firstS != -1) {//take out whichever comes first if both exist
                if (firstE < firstS) {
                    System.out.println("The input with first 'e' or 'E' or 's' or 'S' removed: " + aLine.substring(0, firstE) + aLine.substring(firstE + 1));
                }
                else {
                    System.out.println("The input with first 'e' or 'E' or 's' or 'S' removed: " + aLine.substring(0, firstS) + aLine.substring(firstS + 1));
                }
            }
            else {//letters are not present in either, do nothing or print no e's
                System.out.println("No occurrences of 'e', 'E', 's', or 'S' in string.");
            }
        }
    }
}