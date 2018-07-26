package main

import (
	. "../../queue"
	. "fmt"
	)

type SuperQueue Queue

func main()  {
	q := Queue{1,2,3,4,6,7,8,9}
	q.Push(5)
	q.Pop()
	q.Pop()
	q.Pop()
	Println(q.IsEmpty())
	q.Print()

	s_q := SuperQueue{11,22,33,44}
	println(s_q)

}