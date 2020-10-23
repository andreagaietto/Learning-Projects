public class Utils {
    public static int roll() {
        return (1 + (int)(Math.random() * 6));
    }

    public static int move(int currentPosition, int movementAmount) {
        int initialPosition = currentPosition;
        int finalPosition = 0;
        initialPosition = initialPosition + movementAmount;
        if(initialPosition % 5 == 0) {
            finalPosition = initialPosition + 5;
        }
        else if (initialPosition % 13 == 0) {
            finalPosition = initialPosition - (2 * movementAmount);
        }
        else {
            finalPosition = initialPosition;
        }
        if (finalPosition > 100) {
            finalPosition = finalPosition - 100;
        }
        return finalPosition;
    }
}