package main

import "fmt"

func main() {
	foo()
	bar("Hong")
	s1 := woo("Dong")
	fmt.Println(s1)
	x, y := mouse("Ian", "Fleming")
	fmt.Println(x)
	fmt.Println(y)

	total := foo2(2, 3, 4, 5, 6, 7, 8, 9)
	fmt.Println(total)

}

func foo() {
	fmt.Println("hello from foo")
}

func bar(s string) {
	fmt.Println("Hello,", s)
}

func woo(st string) string {
	return fmt.Sprint("Hello from woo, ", st)
}

func mouse(fn string, ln string) (string, bool) {
	a := fmt.Sprint(fn, ln, `, says "Hello"`)
	b := false
	return a, b
}

func foo2(x ...int) int {
	fmt.Println(x)
	fmt.Printf("%T\n", x)

	sum := 0
	for i, v := range x {
		sum += v
		fmt.Println("for item in index position,", i, "we are now adding,", v, "to the total which is now", sum)
	}
	fmt.Println("The total is,", sum)
	return sum
}