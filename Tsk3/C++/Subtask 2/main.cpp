#include <fstream>
#include <iostream>
#include <string>
int main() {
    std::string script_dir = __FILE__;
    script_dir = script_dir.substr(0, script_dir.find_last_of('/') + 1); 
    // For Linux/macOS, replace '\\' with '/'

    std::string input_filename = "input.txt";
    std::string output_filename = "output.txt";
    std::string input_path = script_dir + input_filename;
    std::string output_path = script_dir + output_filename;

    std::ifstream input_file(input_path);
    if (!input_file.is_open()) {
        std::cerr << "Error: Could not open input file '" << input_filename << "'" << std::endl;
        return 1;
    }
    std::ofstream output_file(output_path);
    if (!output_file.is_open()) {
        std::cerr << "Error: Could not open output file '" << output_filename << "'" << std::endl;
        return 1;
    }
    std::string content;
    std::string line;
    while (std::getline(input_file, line)) {
        content += line + "\n";
    }
    output_file << content;

    input_file.close();
    output_file.close();

    std::cout << "File copied successfully!" << std::endl;
    return 0; 
}