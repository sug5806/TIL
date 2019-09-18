package main

import "fmt"

func main() {
	bd := 1994
	for {
		if bd < 2019{
			n, err := fmt.Println(bd)
			fmt.Println(n, err)

			bd++
			continue
		} else {
			break
		}

	}
}