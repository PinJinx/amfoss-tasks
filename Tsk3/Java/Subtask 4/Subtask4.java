import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Subtask4 {
    public static void main(String[] args) {
        String scriptDir = System.getProperty("user.dir");
        Path inputFilePath = Paths.get(scriptDir, "input.txt");
        Path outputFilePath = Paths.get(scriptDir, "output.txt");

        try {
            String input = Files.readString(inputFilePath).trim();
            int n = Integer.parseInt(input);

            if (n % 2 == 0) {
                n -= 1;
            }
            int k = (n + 1) - 2;
            StringBuilder output = new StringBuilder();
            for (int i = 1; i <= n; i += 2) {
                k -= 1;
                output.append(" ".repeat(k)).append("*".repeat(i)).append("\n");
            }
            for (int i = n - 2; i > 0; i -= 2) {
                k += 1;
                output.append(" ".repeat(k)).append("*".repeat(i)).append("\n");
            }
            Files.writeString(outputFilePath, output.toString());

        } catch (IOException e) {
            System.err.println("error");
            e.printStackTrace();
        }
    }
}
