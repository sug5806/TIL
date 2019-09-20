package main

import "fmt"

type person struct {
	first string
	last  string
	age   int
}

// human 인터페이스를 구현함
func (p *person) speak() {
	fmt.Println(p.first, p.last, p.age)
}

// speak 메서드를 가지는 human 인터페이스 정의
type human interface {
	speak()
}

func saySomething(h human) {
	h.speak()
}

func main() {
	h1 := person{
		first: "James",
		last:  "Bond",
		age:   32,
	}

	h2 := person{
		first: "Miss",
		last: "Moneypenny",
		age: 27,
	}

	saySomething(&h1)
	saySomething(&h2)

}
