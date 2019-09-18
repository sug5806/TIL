package main

import "fmt"

func main() {
	dict := map[string][]string{
		"bond_james": []string{"Shaken, not stirred", "Martinis", "Women"},
		"moneypenny_miss": []string{"James Bond", "Literature", "Computer Science"},
		"no_dr": []string{"Being evil", "Ice cream", "Sunsets"},
	}


	// add map
	dict["dongsu"] = []string{"26", "Seoul", "backend"}
	for k, v := range dict{
		fmt.Println(k, v)
	}

	fmt.Println()

	// delete map
	delete(dict, "dongsu")

	for k, v := range dict{
		fmt.Println(k, v)
	}



}
