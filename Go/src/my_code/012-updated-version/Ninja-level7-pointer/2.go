package main

import "fmt"

type person struct {
	first string
}

func changeMe(p *person) {
	// p가 선언된 포인터 타입이고
	// *p.f가 필드를 나타내는 유효한 경우
	// p.f는 (*p).f의 약어이다.
	p.first = "hong"
	//(*p).first = "zxcv"
}

func main() {
	p1 := person{
		first: "asdf",
	}

	fmt.Println(p1)
	changeMe(&p1)
	fmt.Println(p1)
}
