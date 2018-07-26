package main

import "fmt"

type Phone struct {
	OS string
	Net string
}
type PhonePlus struct {
	Phone
	Plus string
}
type PhoneFunction interface {
    Communicate()
    Online()
}

func Call(OnePhone PhoneFunction) {
	OnePhone.Communicate()
}
func QQ(OnePhone PhoneFunction) {
	OnePhone.Online()
}

func (p Phone) Communicate() {
	fmt.Printf("...呼叫中 \n")
}

func (p Phone) Online() {
	fmt.Printf("...上网中 \n")
}

//// 组合
//type Mi8 struct {
//	Phone
//}

func main() {
	p := &PhonePlus{Phone{"ios", "5G"},"5.0"}
	fmt.Printf("%+v ", p)
	Call(p)
	QQ(p)
	fmt.Printf("%+v ", p.Phone)
	Call(p.Phone)
	QQ(p.Phone)

	//t := Phone{"Android","5G"}
	//fmt.Printf("%+v ", t)
	//Call(t)
	//QQ(t)

}
