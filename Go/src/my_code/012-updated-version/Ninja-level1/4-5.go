package main

import "fmt"

type mt int
var q mt

var y int

func main() {
	fmt.Println(q)
	fmt.Printf("%T\n", q)
	q = 42
	fmt.Println(q)

	y = int(q)
	fmt.Println(y)
	fmt.Printf("%T\n", y)
}