#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH_LENGTH 1024
#define MAX_LINE_LENGTH 1024

int main() {
    char script_dir[MAX_PATH_LENGTH];
    char input_filename[] = "input.txt";
    char output_filename[] = "output.txt";
    char input_path[MAX_PATH_LENGTH];
    char output_path[MAX_PATH_LENGTH];

    char *cwd = getw(script_dir, MAX_PATH_LENGTH);
    if (cwd == NULL) {
        perror("getcwd");
        return 1;
    }

    snprintf(input_path, sizeof(input_path), "%s/%s", script_dir, input_filename);
    snprintf(output_path, sizeof(output_path), "%s/%s", script_dir, output_filename);

    FILE *input_file = fopen(input_path, "r");
    if (input_file == NULL) {
        fprintf(stderr, "Error: Could not open input file '%s'\n", input_filename);
        return 1;
    }

    FILE *output_file = fopen(output_path, "w");
    if (output_file == NULL) {
        fprintf(stderr, "Error: Could not open output file '%s'\n", output_filename);
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), input_file) != NULL) {
        fputs(line, output_file);
    }

    fclose(input_file);
    fclose(output_file);

    printf("File copied successfully!\n");
    return 0;
}