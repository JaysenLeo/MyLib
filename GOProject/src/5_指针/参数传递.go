package main

import "fmt"

func swap_val(a, b int) {
	b, a = a, b
}
func swap_val_res(a, b int) (int, int) {
	b, a = a, b
	return a, b
}
func swap_ref(a, b *int) {
	*b, *a = *a, *b
}

func main() {
	a, b := 1, 2
	fmt.Println(a, b)
	//swap_val(a, b)
	//fmt.Println(a, b)
	swap_ref(&a, &b)
	//a, b = swap_val_res(a, b)
	fmt.Println(a, b)
	// 结构体
}
