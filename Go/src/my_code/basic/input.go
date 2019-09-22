package main

import "fmt"

func main() {
	var text float64
	_, err := fmt.Scanf("%f", &text)
	//_, err := fmt.Scan(&text)
	if err != nil{
		fmt.Println("Error!")
	} else{
		fmt.Printf("%T\n", text)
		fmt.Println(text)
	}






}
