package main

import "fmt"

func main() {
	favSport := "James Bond"
	switch favSport {
	case "James Bond":
		fmt.Println("True1")
		// 다음 case와 비교를 무시하고 실행함
		fallthrough
	case "James bond":
		fmt.Println("True?")

	default:
		fmt.Println("default")
	}
}
