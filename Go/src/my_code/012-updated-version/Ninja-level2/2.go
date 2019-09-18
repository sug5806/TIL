package main

import "fmt"

func main() {
	a := (42 == 42)
	b := (43 <= 45)
	c := (42 >= 40)
	d := (42 != 40)
	e := (40 < 43)
	f := (43 > 23)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(f)
}
