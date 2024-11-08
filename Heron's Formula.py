import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values for a, b, and c
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        // Check if the sides can form a valid triangle
        if (a + b > c && a + c > b && b + c > a) {
            // Calculate semi-perimeter
            double s = (a + b + c) / 2;

            // Calculate the area using Heron's formula
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

            // Print the result with 4 decimal places
            System.out.printf("%.4f", area);
        } else {
            // If not a valid triangle, area is 0.0000
            System.out.printf("%.4f", 0.0);
        }

        scanner.close();
    }
}
