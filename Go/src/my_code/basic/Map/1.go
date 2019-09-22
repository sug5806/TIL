package main

import "fmt"

func main() {
	// key는 string타입, value는 int타입의 맵을 만든다.
	m := map[string]int{
		"James":           32,
		"Miss Moneypenny": 27,
	}
	fmt.Println(m)

	// map에 데이터 추가하기
	m["Dong"] = 26
	fmt.Println(m)

	delete(m, "James")
	fmt.Println(m)

	// map에 없는 ket값을 삭제하려해도 오류가 발생하지 않는다.
	delete(m, "iam Fleming")
	fmt.Println(m)
}
