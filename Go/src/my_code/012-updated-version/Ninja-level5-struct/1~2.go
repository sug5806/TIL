/*
Hands-on exercise #1
Create your own type “person” which will have an underlying type of “struct” so that it can store the following data:
first name
last name
favorite ice cream flavors
Create two VALUES of TYPE person. Print out the values, ranging over the elements in the slice which stores the favorite flavors.
solution:
https://play.golang.org/p/ouRHmH_POg
video: 086
*/

package main

import "fmt"

type person struct {
	first_name                 string
	last_name                  string
	favorite_ice_cream_flavors []string
}

func main() {
	p1 := person{
		first_name: "James",
		last_name:  "Bonds",
		favorite_ice_cream_flavors: []string{
			"mint",
			"chocolate",
			"martini",
		},
	}

	p2 := person{
		first_name: "King",
		last_name:  "God",
		favorite_ice_cream_flavors: []string{
			"vanilla",
			"strawberry",
			"coffee",
		},
	}

	fmt.Println(p1.first_name, p1.last_name)
	for idx, favor := range p1.favorite_ice_cream_flavors{
		fmt.Println(idx, favor)
	}
	fmt.Println(p2.first_name, p2.last_name)
	for idx, favor := range p2.favorite_ice_cream_flavors{
		fmt.Println(idx, favor)
	}

	m := map[string]person{
		p1.last_name: p1,
		p2.last_name: p2,
	}

	for _, v := range m{
		fmt.Println(v.first_name)
		fmt.Println(v.last_name)
		for idx, v := range v.favorite_ice_cream_flavors{
			fmt.Println(idx, v)
		}
	}
}
