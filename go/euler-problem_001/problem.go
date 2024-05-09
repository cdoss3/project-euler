package main

import "fmt"

func main() {
	var total int = 0
	n := 1

	for n < 1000 {
		if n % 3 == 0 {
			total += n
		} else if n % 5 == 0 {
			total += n
		}

		n += 1
	}

	fmt.Printf("%s is the sum of all multiples divisible by 3 or 5", total)
}
