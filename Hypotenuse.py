import java.util.Scanner;

public class HypotenuseCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values for X and Y
        double X = scanner.nextDouble();
        double Y = scanner.nextDouble();

        // Calculate the hypotenuse
        double hypotenuse = Math.sqrt(Math.pow(X, 2) + Math.pow(Y, 2));

        // Print the result with 2 decimal places
        System.out.printf("%.2f", hypotenuse);

        scanner.close();
    }
}