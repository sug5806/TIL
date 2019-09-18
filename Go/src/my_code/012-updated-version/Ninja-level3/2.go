// Hands-on exercise #2
// Print every rune code point of the uppercase alphabet three times. Your output should look like this:
// 65
// U+0041 'A'
// U+0041 'A'
// U+0041 'A'
// 66
// U+0042 'B'
// U+0042 'B'
// U+0042 'B'
// … through the rest of the alphabet characters
// solution: https://play.golang.org/p/1OjnCX1D5H
// video: 051

package main

import "fmt"

func main() {
	x := 65
	for x<91{
		for idx:=0; idx<3; idx++{
			fmt.Printf("%#U\n", x)
		}
		x++;
	}
}