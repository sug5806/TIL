package main

import (
	"fmt"
)

func main() {
	s1 := foo()
	fmt.Println(s1)

	x := bar()

	fmt.Printf("%T\n", x)
	y := x()
	fmt.Println(y)
}

func foo() string {
	s := "Hello world"
	return s
}

func bar() func() int {
	// 익명 함수 자체를 리턴한다.
	return func() int {
		return 451
	}
}
