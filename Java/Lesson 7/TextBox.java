public class TextBox {
    public static String textBoxString(int side) { //method will be used if only one int is provided

        String boxString = ""; //initiate the string

        for (int i = 1; i <= side; i++) { //outer loop controls rows
            if ((i == 1) || (i == side)) { //checks to see if this row is a top or bottom row
                for (int j = 1; j <= side; j++) { //if top or bottom row, print all symbols
                    boxString = boxString + "*";
                }
            }
            else {
                for (int k = 1; k <= side; k++) { //if not a top or bottom row add a symbol or space
                    if ((k == 1) || (k == side)) {
                        boxString = boxString + "*";
                    }
                    else {
                        boxString = boxString + " ";
                    }
                }
            }
            boxString = boxString + "\n"; //new line at end of each row
        }
        return boxString;
    }
    public static String textBoxString(int side, char bChar) { //use if given an int and a char

        String boxString = ""; //initiate string

        for (int i = 1; i <= side; i++) { //control rows
            if ((i == 1) || (i == side)) { //check if a border row
                for (int j = 1; j <= side; j++) { //if border row, print all symbols
                    boxString = boxString + bChar;
                }
            }
            else { //if not a border row, print either a char or a space
                for (int k = 1; k <= side; k++) {
                    if ((k == 1) || (k == side)) {
                        boxString = boxString + bChar;
                    }
                    else {
                        boxString = boxString + " ";
                    }
                }
            }
            boxString = boxString + "\n"; //add new line after each loop
        }
        return boxString;
    }
    public static String textBoxString(int rows, int cols) { //will run if given two ints
        String boxString = ""; //initiate string
        for (int i = 1; i <= rows; i++) { //outer loop to control rows with variable
            if ((i == 1) || (i == rows)) { //check if border row
                for (int j = 1; j <= cols; j++) { //if border row print all asterisks
                    boxString = boxString + "*";
                }
            }
            else { //else print either a space or a symbol
                for (int k = 1; k <= cols; k++) {
                    if ((k == 1) || (k == cols)) {
                        boxString = boxString + "*";
                    }
                    else {
                        boxString = boxString + " ";
                    }
                }
            }
            boxString = boxString + "\n"; //new line after each loop
        }
        return boxString;
    }
    public static String textBoxString(int rows, int cols, char c1, char c2) { //will run if given two ints and two chars
        String boxString = ""; //initiate string
        int printCount = 0; //create counter to check if even or odd char
        for (int i = 1; i <= rows; i++) {//outer loop controls rows
            if ((i == 1) || (i == rows)) { //check if a border row
                for (int j = 1; j <= cols; j++) {
                    if (printCount % 2 == 0) {//check if this is an odd or even printing of a char to determine which to use
                        boxString = boxString + c1;
                        printCount += 1;
                    }
                    else {
                        boxString = boxString + c2;
                        printCount += 1;
                    }
                }
            }
            else {
                for (int k = 1; k <= cols; k++) { //if a center row, print either a space or a char
                    if ((k == 1) || (k == cols)) {
                        if (printCount % 2 == 0) {
                            boxString = boxString + c1;
                            printCount += 1;
                        }
                        else {
                            boxString = boxString + c2;
                            printCount += 1;
                        }
                    }
                    else {
                        boxString = boxString + " ";
                    }
                }
            }
            boxString = boxString + "\n"; //new line after loop
        }
        return boxString;
    }
}