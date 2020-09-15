import javax.swing.*;

public class FlashCard {
    public static void main(String[] args){



        WidgetViewer wv = new WidgetViewer(); //create new WidgetViewer object
        double num1 = (int)(Math.random() * 100) / 10.0;
        double num2 = (int)(Math.random() * 100) / 10.0;


        JLabel jlInstructions = new JLabel("What is " + num1 + " plus " + num2 + "?");
        JTextField userResponse = new JTextField(5);

        wv.add(jlInstructions, 10, 30, 300, 20);
        wv.add(userResponse, 10, 50, 50, 20);
        JButton execute = new JButton("click after answering");
        wv.addAndWait(execute);

        double n1 = Double.parseDouble(userResponse.getText());

        if (n1 == (num1 + num2)) {
            JLabel correct = new JLabel("Good Job");
            wv.add(correct, 10, 80, 300, 20);
        }
        else {
            JLabel wrong = new JLabel("Sorry, the correct answer is " + (num1 + num2));
            wv.add(wrong, 10, 80, 300, 20);
        }

    }
}