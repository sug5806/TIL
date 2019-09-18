package main

import "fmt"

func main() {
	sli := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}

	for i, v := range sli{
		fmt.Println(i, v)
	}

	fmt.Printf("%T\n", sli)

	fmt.Println(sli[:5])
	fmt.Println(sli[5:])
	fmt.Println(sli[2:7])
	fmt.Println(sli[1:6])


}