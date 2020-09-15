import javax.swing.*;

public class Operation {
    public static void main(String[] args) {
        WidgetViewer wv = new WidgetViewer();

        String solution = "";
        int operation;

        int x = 1 + (int)(Math.random() * 9);
        int y = 1 + (int)(Math.random() * 9);

        JLabel displayX = new JLabel("x is " + x);
        JLabel displayY = new JLabel("y is " + y);
        JLabel displayInstructions = new JLabel("Enter an operation number");
        JTextField userResponse = new JTextField(5);


        wv.add(displayX, 10, 30, 300, 20);
        wv.add(displayY, 10, 40, 300, 20);
        wv.add(displayInstructions, 10, 50, 300, 20);
        wv.add(userResponse, 10, 70, 50, 20);
        JButton execute = new JButton("Press here when you've entered your operation");
        wv.addAndWait(execute);

        operation = Integer.parseInt(userResponse.getText());

        if (operation >= 1 && operation <= 10) {
            solution = (x * y) + "";
        }
        else if ((operation % 4) == 0) {
            solution = (x + y) + "";
        }
        else if ((operation % 5) == 0) {
            solution = String.format("%.2f",((float)x / y));
        }
        else if ((operation % 2) == 0) {
            solution = (y / x) + "";
        }
        else {
            solution = (y - x) + "";
        }

        JLabel displayResult = new JLabel("This is the solution: " + solution);
        wv.add(displayResult, 10, 90, 300, 20);
    }
}