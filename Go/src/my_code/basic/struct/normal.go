package main

import "fmt"

type person struct {
	first string
	last  string
	age   int
}

type secretAgent struct {
	person
	first string
	ltk bool
}

func main() {
	sa1 := secretAgent{
		person: person{
				first : "James",
				last: "Bond",
				age: 32,
		},
		first: "somethin cool",
		ltk: true,
	}

	p2 := person{
		first: "Miss",
		last:  "Moneypenny",
		age:   27,
	}

	fmt.Println(sa1)
	fmt.Println(p2)

	// age의 경우 person 타입의 필드이나 secreAgent의 필드로 승격이 되었다.
	fmt.Println(sa1.person.first, sa1.first, sa1.person.last, sa1.age, sa1.ltk)
	fmt.Println(p2.first, p2.last, p2.age)

}
