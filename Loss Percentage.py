import java.util.Scanner;

public class LossPercentageCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values for Cost Price (CP) and Selling Price (SP)
        double CP = scanner.nextDouble();
        double SP = scanner.nextDouble();

        // Calculate the loss
        double loss = CP - SP;

        // Calculate the loss percentage
        double lossPercentage = (loss / CP) * 100;

        // Print the loss percentage with 2 decimal places
        System.out.printf("%.2f", lossPercentage);

        scanner.close();
    }
}
