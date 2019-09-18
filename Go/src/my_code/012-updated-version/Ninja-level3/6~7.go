package main

import "fmt"

func main() {
	str := "James Bond"
	if str == "James bond" {
		fmt.Println("True1")
	} else if str == "James Bond" {
		fmt.Println("True2")
	} else {
		fmt.Println("False")
	}

}
