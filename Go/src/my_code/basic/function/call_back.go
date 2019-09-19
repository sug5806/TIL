package main

import (
	"fmt"
)

func main() {
	ii := []int{1, 2, 3, 4, 5, 6, 7, 8, 9,}
	s := sum(ii...)
	fmt.Println("all sum:", s)

	e := even(sum, ii...)
	fmt.Println("even sum:", e)

	o := odd(sum, ii...)
	fmt.Println("odd sum:", o)
}

func sum(xi ...int) int {
	fmt.Printf("%T\n", xi)
	total := 0
	for _, v := range xi {
		total += v
	}
	return total
}

// 리턴값이 int인 함수와 길이제한 없는 슬라이스를 파라미터로 받고 리턴은 int로 한다.
func even(f func(xi ...int) int, vi ...int) int {
	var yi []int
	for _, v := range vi {
		if v%2 == 0 {
			yi = append(yi, v)
		}
	}
	// 파라미터로 받은 함수 f를 yi인자를 넘겨주고 호출한다.
	// 호출하고 리턴받은 값을 리턴한다.
	return f(yi...)
}

func odd(f func(xi ...int) int, vi ...int) int {
	var xi []int
	for _, v := range vi {
		if v%2 == 1 {
			xi = append(xi, v)
		}
	}

	return f(xi...)
}
