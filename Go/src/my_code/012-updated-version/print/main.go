package main

import (
	"fmt"
)

var y = 42

func main() {
	// 값 출력
	fmt.Println(y)
	// 타입 출력
	fmt.Printf("%T\n", y)
	// 2진수 출력
	fmt.Printf("%b\n", y)
	// 16진수 출력
	fmt.Printf("%x\n", y)
	// 0x를 포함한 소문자로 16진수 출력
	fmt.Printf("%#x\n", y)
	// 0X를 포함한 대문자로 16진수 출력
	fmt.Printf("%#X\n", y)

	y = 911

	fmt.Printf("%#x\t%b\t%x\n", y, y, y)
	s := fmt.Sprintf("%#x\t%b\t%x\n", y, y, y)
	fmt.Println(s)
	fmt.Printf("%v", y)
}
