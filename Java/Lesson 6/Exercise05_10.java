public class Exercise05_10 {
    public static void main(String[] args) {

        int lineCount = 0;

        for (int i = 100; i <= 1000; i++) {
            if ((i % 5 == 0) && (i % 6 == 0)) {
                if (lineCount <= 9) {
                    System.out.print(i + " ");
                    lineCount ++;
                }
                else {
                    System.out.println();
                    System.out.print(i + " ");
                    lineCount = 1;
                }
            }
        }
    }
}