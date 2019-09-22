package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

var CLOSEA = false
var DATA = make(map[int]bool)

func random(min, max int) int{
	return rand.Intn(max-min) + min
}

// out채널은 쓰기만 가능
func first(min, max int, out chan<- int){
	for {
		// CLOSEA가 true면 채널 닫기
		if CLOSEA {
			close(out)
			return
		}
		// out채널에 랜덤값을 쓴다
		out <- random(min, max)
	}
}

// in 채널로부터 데이터를 받아서 out채널로 데이터를 보낸다
func second(out chan<- int, in <-chan int){
	for x := range in {
		fmt.Print(x, " ")
		_, ok := DATA[x]
		if ok {
			CLOSEA = true
		} else{
			DATA[x] = true
			out <- x
		}
	}
	fmt.Println()
	close(out)
}

// in채널로부터 계속 값을 읽는다.
func third(in <-chan int){
	var sum int
	sum = 0
	for x2 := range in{
		sum = sum + x2
	}
	fmt.Printf("The sum of the random numbers is %d\n", sum)
}

func main() {
	if len(os.Args) != 3{
		fmt.Println("Need two integer parameters!")
		os.Exit(1)
	}

	// Atoi를 통해 문자열을 정수로 바꿈
	n1, _ := strconv.Atoi(os.Args[1])
	n2, _ := strconv.Atoi(os.Args[2])

	if n1 >n2 {
		fmt.Printf("%d should be smaller than %d\n", n1, n2)
		return
	}

	rand.Seed(time.Now().UnixNano())
	// 쓰기용채널 A
	A := make(chan int)
	// 읽기용채널 B
	B := make(chan int)

	go first(n1, n2, A)
	go second(B, A)
	third(B)
}
