package main

import "fmt"

func main() {
	fmt.Println("1") // 1
	defer foo() // 스택?에 첫번째로 쌓임
	defer bar() // 스택?에 2번째로 쌓임
	fmt.Println("2")
	fmt.Println("3")
	fmt.Println("4")
	fmt.Println("5")
	fmt.Println("6")
}

func foo() {
	defer func() {
		fmt.Println("7")
	}()
	fmt.Println("8")
	fmt.Println("9")
	fmt.Println("10")
}

func bar(){
	fmt.Println("11")
}