package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

func main() {
	// Get the directory of the current script
	scriptDir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		fmt.Println("Error getting the script directory:", err)
		return
	}

	// Define input and output file paths
	inputFilePath := filepath.Join(scriptDir, "input.txt")
	outputFilePath := filepath.Join(scriptDir, "output.txt")

	// Read content from the input file
	content, err := ioutil.ReadFile(inputFilePath)
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	// Write content to the output file
	err = ioutil.WriteFile(outputFilePath, content, 0644)
	if err != nil {
		fmt.Println("Error writing output file:", err)
		return
	}

	fmt.Println("File content copied successfully.")
}
