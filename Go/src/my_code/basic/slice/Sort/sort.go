package Sort

import (
	"fmt"
	"sort"
)

func main() {
	xi := []int{4, 7, 3, 42, 99, 18, 16, 56, 12}
	xs := []string{"James", "Q", "M", "Moneypenny", "Dr. No"}

	// Ints와 Strings는 리턴값이 없다

	fmt.Println(xi)
	sort.Ints(xi)
	fmt.Println(xi)

	fmt.Println("----------------")

	fmt.Println(xs)
	sort.Strings(xs)
	fmt.Println(xs)

	//nx := sort.IntSlice{5, 7, 1, 6, 9}
	//nx.Sort()
	//fmt.Println(nx)


}
