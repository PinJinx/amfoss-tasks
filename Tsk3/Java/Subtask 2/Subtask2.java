import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    public static void Subtask2(String[] args) {
        // Get the directory of the current working directory
        String scriptDir = System.getProperty("user.dir");

        // Create file paths for input and output files
        Path inputFilePath = Paths.get(scriptDir, "input.txt");
        Path outputFilePath = Paths.get(scriptDir, "output.txt");

        try {
            if (!Files.exists(inputFilePath)) {
                System.err.println("Input file does not exist: " + inputFilePath);
                return;
            }
            String content = Files.readString(inputFilePath);
            Files.writeString(outputFilePath, content);
            System.out.println("File copied successfully!");

        } catch (IOException e) {
            System.err.println("An error occurred while copying the file:");
            e.printStackTrace();
        }
    }
}
