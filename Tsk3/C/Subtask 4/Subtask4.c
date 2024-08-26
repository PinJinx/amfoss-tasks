#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH_LENGTH 1024

int main() {
    char script_dir[MAX_PATH_LENGTH];
    char input_path[MAX_PATH_LENGTH];
    char output_path[MAX_PATH_LENGTH];

    // Replace with platform-specific code to get script directory
    // For example, on Linux:
    // char *cwd = getcwd(script_dir, MAX_PATH_LENGTH);
    // if (cwd == NULL) {
    //     perror("getcwd");
    //     return 1;
    // }

    strcpy(input_path, script_dir);
    strcat(input_path, "input.txt");
    strcpy(output_path, script_dir);
    strcat(output_path, "output.txt");

    FILE *input_file = fopen(input_path, "r");
    if (input_file == NULL) {
        fprintf(stderr, "Error: Could not open input file\n");
        return 1;
    }

    FILE *output_file = fopen(output_path, "w");
    if (output_file == NULL) {
        fprintf(stderr, "Error: Could not open output file\n");
        return 1;
    }

    int n;
    if (fscanf(input_file, "%d", &n) == 1) {
        if (n % 2 == 0) {
            n--;
        }

        int k = (n + 1) / 2 - 1;

        for (int i = 1; i <= n; i += 2) {
            for (int j = 0; j < k; ++j) {
                fprintf(output_file, " ");
            }
            for (int j = 0; j < i; ++j) {
                fprintf(output_file, "*");
            }
            fprintf(output_file, "\n");
            k--;
        }

        k = 1;
        for (int i = n - 2; i > 0; i -= 2) {
            for (int j = 0; j < k; ++j) {
                fprintf(output_file, " ");
            }
            for (int j = 0; j < i; ++j) {
                fprintf(output_file, "*");
            }
            fprintf(output_file, "\n");
            k++;
        }
    } else {
        fprintf(stderr, "Error: Could not read integer from input file.\n");
        return 1;
    }

    fclose(input_file);
    fclose(output_file);
    return 0;
}