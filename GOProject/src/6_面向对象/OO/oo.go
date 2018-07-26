package main

import "fmt"

type Phone struct {
	OS string
	Net string
}

func (p *Phone) Call() {
	fmt.Printf("...呼叫中 \n")
}

//// 组合
//type Mi8 struct {
//	Phone
//}

func main() {
	p := &Phone{"ios", "5G"}
	fmt.Printf("%+v ", p)
	p.Call()

	t := Phone{"Android","5G"}
	fmt.Printf("%+v ", t)
	t.Call()

}
