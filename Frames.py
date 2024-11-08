import java.util.Scanner;

public class WireframeCostCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values for N, M, and X
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int X = scanner.nextInt();

        // Calculate the cost of the wireframe
        int cost = 2 * (N + M) * X;

        // Output the cost
        System.out.println(cost);

        scanner.close();
    }
}
