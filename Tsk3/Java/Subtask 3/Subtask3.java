import java.util.Scanner;

public class Subtask3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a val: ");
        int n = scanner.nextInt();
        if (n % 2 == 0) {
            n -= 1;
        }
        int k = (n + 1) - 2;
        for (int i = 1; i <= n; i += 2) {
            k -= 1;
            printPatternLine(k, i);
        }
        for (int i = n - 2; i > 0; i -= 2) {
            k += 1;
            printPatternLine(k, i);
        }
        scanner.close();
    }

    private static void printPatternLine(int spaces, int stars) {
        for (int j = 0; j < spaces; j++) {
            System.out.print(' ');
        }
        for (int j = 0; j < stars; j++) {
            System.out.print('*');
        }
        System.out.println();
    }
}
