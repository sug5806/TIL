package main

import "fmt"

func main() {
	vi := []int{1, 2, 3, 4, 5}

	total1 := foo(vi ...)
	total2 := bar(vi)
	fmt.Println(total1)
	fmt.Println(total2)

}

func foo(x ... int) int{
	result := 0
	for _, v := range x{
		result += v
	}
	return result
}

func bar(y []int) int{
	result := 0
	for _,v := range y{
		result += v
	}
	return result
}