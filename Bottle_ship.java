import java.util.Scanner;

public class BottleShipping {
    public static void shipBottles(int numBottles) {
        int xl = numBottles / 48;
        numBottles = numBottles % 48;

        int large = numBottles / 24;
        numBottles = numBottles % 24;

        int medium = numBottles / 12;
        numBottles = numBottles % 12;

        int small = numBottles / 6;

        System.out.print(xl + " xl, " + large + " large, " + medium + " medium, " + small + " small");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of bottles: ");
        int inputBottles = scanner.nextInt();
        shipBottles(inputBottles);
    }
}

