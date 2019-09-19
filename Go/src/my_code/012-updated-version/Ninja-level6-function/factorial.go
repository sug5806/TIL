package main

import (
	"fmt"
)

func main() {
	result := fac(5)
	fmt.Println(result)
	fi := fibo(6)
	fmt.Println(fi)
}

func fac(x int) int{
	if x == 1{
		return 1
	}
	result := x * fac(x-1)
	return result
}

func fibo(y int) int{
	if y == 1 || y == 2{
		return 1
	}
	result := fibo(y-1) + fibo(y-2)
	return result
}

