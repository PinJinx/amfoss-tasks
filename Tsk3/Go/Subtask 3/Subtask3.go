package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Print("Enter a val: ")
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}
	if n%2 == 0 {
		n -= 1
	}
	k := (n + 1) - 2
	for i := 1; i <= n; i += 2 {
		k -= 1
		fmt.Printf("%s%s\n", repeat(" ", k), repeat("*", i))
	}
	for i := n - 2; i > 0; i -= 2 {
		k += 1
		fmt.Printf("%s%s\n", repeat(" ", k), repeat("*", i))
	}
}
func repeat(char string, count int) string {
	result := ""
	for i := 0; i < count; i++ {
		result += char
	}
	return result
}
