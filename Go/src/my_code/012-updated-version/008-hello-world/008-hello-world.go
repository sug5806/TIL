package _08_hello_world

import "fmt"

func main() {
	fmt.Println("Hello everyone, this is the most " +
		"and learning the GO programming language.")
	foo()
	fmt.Println("something more")

	for i := 0; i < 100; i++ {
		if i%2 == 0 {
			fmt.Println(i)
		}
	}

	bar()

}

func foo() {
	n, err := fmt.Println("I'm in foo", 42, true)
	fmt.Println(n)
	fmt.Println(err)
}

func bar() {
	fmt.Println("and then we exited")
}

// control flow:
// (1) sequence
//(2) loop, iterative
//(3) conditional
