package main

import (
	"fmt"
	"time"
)

func A(a, b chan struct{}){
	<-a
	fmt.Println("A()!")
	time.Sleep(time.Second)
	close(b)
}

func B(a, b chan struct{}){
	<-a
	fmt.Println("B()!")
	close(b)
}

func C(a chan struct{}){
	<-a
	fmt.Println("C()!")
}

func main() {
	x := make(chan struct{})
	y := make(chan struct{})
	z := make(chan struct{})

	go C(z)
	// x에 대한 채널을 A함수가 가장 먼저 가져가?므로 A,B,C,C,C가 출력
	go A(x, y)
	go C(z)
	go B(y, z)
	go C(z)

	close(x)
	time.Sleep(3 * time.Second)
}
