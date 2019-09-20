package main

func main() {
	var a interface{} = 1

	i := a
	j := a.(int)

	println(a)
	println(i)
	println(j)
}
