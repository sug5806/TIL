package main

import "fmt"

func main() {
	x := foo()
	a, b := bar()
	fmt.Println(x, a, b)
}

func foo() int {
	return 1
}

func bar() (int, string){
	return 2, "big brother"
}