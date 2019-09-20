package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	incrementer := 0
	gs := 100
	wg.Add(gs)

	var mt sync.Mutex

	for i := 0; i < gs; i ++{
		go func() {
			mt.Lock()
			v := incrementer
			//runtime.Gosched()
			v++
			incrementer = v
			fmt.Println(i, incrementer)
			mt.Unlock()
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("end value: ", incrementer)
}
