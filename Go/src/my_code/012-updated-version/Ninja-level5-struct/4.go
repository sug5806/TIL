/*
Hands-on exercise #4
Create and use an anonymous struct.
solution: https://play.golang.org/p/otBHFs-lPp
video: 089

*/

package main

import "fmt"

func main() {
	s := struct {
		first     string
		friends   map[string]int
		favDrinks []string
	}{
		first: "James",
		friends: map[string]int{
			"Moneypenny": 555,
			"Q":          777,
			"M":          888,
		},
		favDrinks: []string{
			"Martini",
			"Water",
		},
	}
	fmt.Println(s.first)
	fmt.Println(s.friends)
	fmt.Println(s.favDrinks)
	fmt.Println()

	fmt.Printf("%v's friends\n", s.first)
	for k,v := range s.friends{
		fmt.Println(k, v)
	}
	fmt.Println()

	fmt.Printf("%v favDrinks lists\n", s.first)
	for i, val := range s.favDrinks{
		fmt.Println(i, val)
	}


}
