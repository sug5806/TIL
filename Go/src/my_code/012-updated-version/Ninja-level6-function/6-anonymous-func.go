package main

import (
	"fmt"
)

func main() {
	func() {
		fmt.Println("hello anonymous func")
	}()
}
