package main

import(
	"fmt"
	"time"
)

func writeToChannel(c chan int, x int){
	fmt.Println(x)
	// x의 값을 채널 c에 쓴다.
	// c 채널에 쓴 값을 아무도 읽지 않기때문에
	// block 당한다.
	c <- x
	close(c)
	fmt.Println(x)
}

func main() {
	// int타입의 채널을 생성한다
	c := make(chan int)

	go writeToChannel(c, 10)
	time.Sleep(1 * time.Second)
}
