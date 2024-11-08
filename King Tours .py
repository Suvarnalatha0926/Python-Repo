import java.util.Scanner;

public class KingTours {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values for N and M
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        // Calculate the maximum number of people
        int maxPeople = (N * 5) + (M * 7);

        // Output the result
        System.out.println(maxPeople);

        scanner.close();
    }
}
