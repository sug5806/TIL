package main

import "fmt"

func main() {
	f := foo()
	// 변수의 상태를 저장하고있음?
	fmt.Println(f())
	fmt.Println(f())

	// 주소가 다르므로 변수 초기화
	g := foo()
	fmt.Println(g())
	fmt.Println(g())
	fmt.Println(g())
	fmt.Println(g())

}

func foo() func() int {
	x := 0
	return func() int {
		x++
		return x
	}
}
