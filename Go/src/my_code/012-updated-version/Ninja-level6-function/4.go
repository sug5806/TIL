package main

import (
	"fmt"
)

type person struct {
	first string
	last string
	age int
}

func (p person) speak() {
	fmt.Println(p.first, p.last, p.age)
}

func main() {
	p1 := person{
		first: "James",
		last: "Bond",
		age: 32,
	}

	p2 := person{
		first: "Ms",
		last:  "Moneypenny",
		age:   27,
	}

	p1.speak()
	p2.speak()
}