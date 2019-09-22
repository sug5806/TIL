package main

import (
	"fmt"
	"math"
)

// Shape 인터페이스 정의
type Shape interface {
	area() float64
	perimeter() float64
}

// Rect 정의
type Rect struct {
	width, height float64
}

// Circle 정의
type Circle struct {
	radius float64
}

// Rect 타입에 대한 Shape 인터페이스 구현
func (r Rect) area() float64 {
	return r.width * r.height
}

func (r Rect) perimeter() float64 {
	return 2 * (r.width + r.height)
}

// Circle 타입에 대한 Shape 인터페이스 구현

func (c Circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c Circle) perimeter() float64 {
	return 2 * math.Pi * c.radius
}

func main() {
	r := Rect{
		width:  10.,
		height: 20.,
	}

	c := Circle{
		radius: 5.,
	}

	showArea(r, c)

	Calculate(r)
	Calculate(c)
}

// 함수의 파라미터로 Shape 인터페이스를 받겠다
// Shape 인터페이스를 구현한 Circle과 Rect를 받을 수 있다.
func showArea(shape ...Shape) {
	for _, s := range shape {
		a := s.area()
		fmt.Println("area: ", a)
	}
}

func Calculate(x Shape){
	_, ok := x.(Circle)

	if ok {
		fmt.Println("Is a circle!")
	} else{
		fmt.Println(("Is a Rect!: "))
	}

	fmt.Println(x.area())
	fmt.Println(x.perimeter())

}
