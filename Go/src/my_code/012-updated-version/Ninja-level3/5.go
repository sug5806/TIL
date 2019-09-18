package main

import "fmt"

func main() {
	for x := 10; x <= 100; x++ {
		fmt.Printf("remainder (modulus) divied by 4 %v %v\n", x, x%4)
	}
}
