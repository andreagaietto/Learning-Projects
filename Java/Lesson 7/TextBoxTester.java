public class TextBoxTester {
    public static void main(String[] args) {
        System.out.print(TextBox.textBoxString(3));
        System.out.print(TextBox.textBoxString(4, '+'));
        System.out.print(TextBox.textBoxString(3, 4));
        System.out.print(TextBox.textBoxString(3, 5, 'x', 'o'));
    }
}