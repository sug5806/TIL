package main

import (
	"fmt"
	"sort"
)

type aStructure struct {
	person string
	height int
	weight int
}

func main() {
	mySlice := make([]aStructure, 0)
	mySlice = append(mySlice, aStructure{"Mihalis", 180, 90})
	mySlice = append(mySlice, aStructure{"Bill", 134, 45})
	mySlice = append(mySlice, aStructure{"Marietta", 155, 45})
	mySlice = append(mySlice, aStructure{"Epifanios", 144, 50})
	mySlice = append(mySlice, aStructure{"Athina", 134, 40})

	fmt.Println("정렬전:", mySlice)
	// sort.Slice()함수는 정렬 함수의 실행 결과에 따라 슬라이스에 담긴 원소의 순서를 바꾼다.
	sort.Slice(mySlice, func(i, j int) bool {
		return mySlice[i].height < mySlice[j].height
	})
	// sort.SliceIsSorted함수는 제공된 슬라이스가 주어진 함수에대해 정렬되었는지 확인함
	bl := sort.SliceIsSorted(mySlice, func(i, j int) bool {
		return mySlice[i].height < mySlice[j].height
	})
	fmt.Println("키 오름차순:", mySlice, bl)

	sort.Slice(mySlice, func(i, j int) bool {
		return mySlice[i].height > mySlice[j].height
	})
	bl = sort.SliceIsSorted(mySlice, func(i, j int) bool {
		return mySlice[i].height > mySlice[j].height
	})
	fmt.Println("키 내림차순:", mySlice, bl)

}
