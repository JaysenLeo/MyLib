package main

import "fmt"

func main() {
	var name = "Lee"
	// 同C语言，用 & 取地址
	var p_name *string = &name
	// *p_name 取值
	*p_name = "Leee"
	fmt.Println(name)
}
