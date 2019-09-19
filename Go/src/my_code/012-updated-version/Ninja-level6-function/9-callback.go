package main

import "fmt"

func main() {
	g := func(xi []int) int {
		if len(xi) == 0 {
			return 0
		}
		if len(xi) == 1 {
			return xi[0]
		}
		return xi[0] + xi[len(xi)-1]
	}

	result := foo(g, []int{1, 2, 3, 4, 5, 6})
	fmt.Println(result)

}
// 파라미터로 함수와 슬라이스를 받고 인트를 리턴한다
func foo(f func(xi []int) int, ii []int) int{
	// 넘겨받은 함수로 슬라이스를 인자로 넣어 실행
	n := f(ii)
	n++
	return n
}