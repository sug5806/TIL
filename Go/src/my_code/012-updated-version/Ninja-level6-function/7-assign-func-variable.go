package main

import (
	"fmt"
)

func main() {
	a := foo()
	fmt.Println(a)
}

func foo() string{
	return fmt.Sprint("hello")
}