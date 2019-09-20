package main

import (
	"fmt"
	"math"
)

type square struct {
	length float64
}
type circle struct {
	radius float64
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (s square) area() float64 {
	return s.length * s.length
}

// area 메서드를 가지는 인터페이스 정의
type shape interface {
	area() float64
}

func info(s shape) {
	// 인터페이스의 메소드를 호출하면
	// 인터페이스에 담긴 실제타입의 메소드가 호출된다.
	fmt.Println(s.area())
}

func main() {
	sq := square{length: 3.5}
	ci := circle{radius: 2.5}

	s1 := sq
	s2 := ci

	s1.area()
	s2.area()

	info(sq)
	info(ci)
}
