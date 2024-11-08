import java.util.Scanner;

public class ProfitPercentage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values for Cost Price (CP) and Selling Price (SP)
        double CP = scanner.nextDouble();
        double SP = scanner.nextDouble();

        // Calculate the profit
        double profit = SP - CP;

        // Calculate the profit percentage
        double profitPercentage = (profit / CP) * 100;

        // Print the profit percentage with 2 decimal places
        System.out.printf("%.2f", profitPercentage);

        scanner.close();
    }
}
