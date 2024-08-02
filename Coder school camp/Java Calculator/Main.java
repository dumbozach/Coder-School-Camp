import java.util.Scanner;

public class Main {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("What is your first number");
            int num1 = scanner.nextInt();

            System.out.println("What is your symbol?");
            char symbol = scanner.next().charAt(0);

            System.out.println("What is your second number?");
            int num2 = scanner.nextInt();

            switch (symbol) {
                case '+' -> System.out.println("Your answer is "+(num1 + num2));
                case '-' -> System.out.println("Your answer is "+(num1 - num2));
                case '*' -> System.out.println("Your answer is "+(num1 * num2));
                case '/' -> System.out.println("Your answer is "+(num1/num2));
                case 'x' -> System.out.println("Your answer is "+Math.pow(num1, num2));
                default -> System.out.println("Invalid symbol");
            }
        }
    }
}