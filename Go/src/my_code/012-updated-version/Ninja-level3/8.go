package main

import "fmt"

func main() {
	// switch에 조건식이 없으면 기본값은 true이다
	switch{
	case true:
		fmt.Println("True")
	case false:
		fmt.Println("False")
	}

}
