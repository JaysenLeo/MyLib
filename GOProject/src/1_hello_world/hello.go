package main

import (
	"fmt"
	"os"
)

func main() {
	guest := "Lee"
	if len(os.Args) > 1 {
		/*
				在终端下输入
				E:\GOProject\src\1_hello_world>go_build_hello_go.exe hehe
				知识点一 os.Args[0] 是 go_build_hello_go.exe
			   	知识点二 os.Args[1] 是 hehe
		*/
		guest = os.Args[1]
		fmt.Println("guest", os.Args[0])
	}
	fmt.Println("Hello", guest)
}
