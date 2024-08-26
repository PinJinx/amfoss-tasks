package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func main() {
	scriptDir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		fmt.Println("Error getting the script directory:", err)
		return
	}

	inputFilePath := filepath.Join(scriptDir, "input.txt")
	outputFilePath := filepath.Join(scriptDir, "output.txt")

	input, err := ioutil.ReadFile(inputFilePath)
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	n, err := strconv.Atoi(strings.TrimSpace(string(input)))
	if err != nil {
		fmt.Println("Error converting input to integer:", err)
		return
	}

	if n%2 == 0 {
		n -= 1
	}

	k := (n + 1) - 2

	f2, err := os.Create(outputFilePath)
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}
	defer f2.Close()

	for i := 1; i <= n; i += 2 {
		k -= 1
		line := strings.Repeat(" ", k) + strings.Repeat("*", i) + "\n"
		_, err := f2.WriteString(line)
		if err != nil {
			fmt.Println("Error writing to output file:", err)
			return
		}
	}

	for i := n - 2; i > 0; i -= 2 {
		k += 1
		line := strings.Repeat(" ", k) + strings.Repeat("*", i) + "\n"
		_, err := f2.WriteString(line)
		if err != nil {
			fmt.Println("Error writing to output file:", err)
			return
		}
	}

	fmt.Println("Pattern successfully written to", outputFilePath)
}
