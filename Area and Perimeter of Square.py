import java.util.Scanner;

public class SquareAreaPerimeter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the side of the square
        int side = scanner.nextInt();

        // Calculate the area
        int area = side * side;

        // Calculate the perimeter
        int perimeter = 4 * side;

        // Print the area and perimeter
        System.out.println(area + " " + perimeter);

        scanner.close();
    }
}
