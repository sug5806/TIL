package main

import (
	"fmt"
	"runtime"
	"sync"
	//"time"
)

func main() {
	fmt.Println("CPUs: ", runtime.NumCPU())
	fmt.Println("Goroutines: ", runtime.NumGoroutine())

	counter := 0

	const gs = 100
	var wg sync.WaitGroup
	wg.Add(gs)

	var my sync.Mutex

	for i := 0; i < gs; i++ {
		// 익명함수
		go func() {
			// race condition을 방지하기 위함
			my.Lock()
			v := counter
			//time.Sleep(time.Second * 2)
			runtime.Gosched()
			v++
			counter = v
			my.Unlock()
			wg.Done()
		}()
		fmt.Println("Goroutines: ", runtime.NumGoroutine())
	}
	wg.Wait()
	fmt.Println("Goroutines: ", runtime.NumGoroutine())
	fmt.Println("count: ", counter)
}
