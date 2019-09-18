package main

import "fmt"

func main() {
	x := []string{"James", "Bond", "Shaken, not stirred"}
	y := []string{"Miss", "Moneypenny", "Hellooooooo, James"}
	z := [][]string{x, y}

	for idx, v := range z{
		fmt.Println("record: ", idx)
		for j, val := range v{
			fmt.Printf("index position: %v \t value: %s\n", j, val)
		}
	}


}
