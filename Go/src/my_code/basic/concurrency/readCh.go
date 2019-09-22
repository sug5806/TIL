package main

import (
	"fmt"
	"time"
)

func writeToChannel(c chan int, x int){
	fmt.Println("1", x)
	c <- x
	close(c)
	fmt.Println("2", x)
}

// 채널 C는 쓰기 전용으로만 사용가능하다.
func f1(c chan<- int, x int){
	fmt.Println(x)
	c <- x
}
// out은 쓰기전용, in은 출력전용 채널이다.
func f2(out chan<- int64, in <-chan int64){
	fmt.Println(x)
	c <- x
}

func main() {
	c := make(chan int)
	go writeToChannel(c, 10)
	time.Sleep(1 * time.Second)
	fmt.Println("Read:", <-c)
	time.Sleep(1*time.Second)

	_, ok := <-c
	if ok {
		fmt.Println("Channel is open!")
	} else{
		fmt.Println("Channel is closed!")
	}
}
