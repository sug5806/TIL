package concurrency

import (
	"fmt"
	"runtime"
	"sync"
)

// WaitGroup 생성, 2개의 Go루틴을 기다림.
var wg sync.WaitGroup


func main() {
	fmt.Println("OS\t", runtime.GOOS)
	fmt.Println("ARCH\t", runtime.GOARCH)
	fmt.Println("CPUs\t", runtime.NumCPU())
	fmt.Println("Goroutines\t", runtime.NumGoroutine())
	wg.Add(2)
	go foo()
	go bar()

	fmt.Println("CPUs\t", runtime.NumCPU())
	fmt.Println("Goroutines\t", runtime.NumGoroutine())
	wg.Wait()
}

func foo() {
	for i := 0; i< 10; i++{
		fmt.Println("foo: ", i)
	}
	wg.Done()
}

func bar() {
	for i := 0; i< 10; i++{
		fmt.Println("bar: ", i)
	}
	wg.Done()
}