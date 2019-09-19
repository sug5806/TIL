package main

import (
	"fmt"
)

func main() {
	f := foo()
	fmt.Println(f())

}
// 정수를 리턴하는 함수를 리턴한다.
func foo() func() int{
	return func() int{
		return 42
	}
}