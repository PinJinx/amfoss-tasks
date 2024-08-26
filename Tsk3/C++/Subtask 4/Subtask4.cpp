#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main() {
    string script_dir = __FILE__;
    script_dir = script_dir.substr(0, script_dir.find_last_of('/') + 1);
    string input_path = script_dir + "input.txt";
    string output_path = script_dir + "output.txt";

    ifstream input_file(input_path);
    if (!input_file.is_open()) {
        cerr << "Error: Could not open input file" << endl;
        return 1;
    }

    ofstream output_file(output_path);
    if (!output_file.is_open()) {
        cerr << "Error: Could not open output file" << endl;
        return 1;
    }

    int n;
    if (input_file >> n) {
        if (n % 2 == 0) {
            n--; 
        }

        int k = (n + 1) / 2 - 1;

        for (int i = 1; i <= n; i += 2) {
            for (int j = 0; j < k; ++j) {
                output_file << " ";
            }
            for (int j = 0; j < i; ++j) {
                output_file << "*";
            }
            output_file << endl;
            k--;
        }

        k = 1;
        for (int i = n - 2; i > 0; i -= 2) {
            for (int j = 0; j < k; ++j) {
                output_file << " ";
            }
            for (int j = 0; j < i; ++j) {
                output_file << "*";
            }
            output_file << endl;
            k++;
        }
    } else {
        cerr << "Error: Could not read integer from input file." << endl;
        return 1;
    }

    input_file.close();
    output_file.close();
    return 0;
}