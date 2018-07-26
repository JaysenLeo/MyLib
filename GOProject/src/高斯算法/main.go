package main

import "fmt"

func main()  {
	sum1 := 0
	for i:= 1;i<=100;i++{
		sum1 += i
	}
	fmt.Println("非高斯算法 %d ",sum1)

	head := 1
	last, num := 100, 100
	sum2 := (head + last) * num / 2
	fmt.Println("高斯算法 %d", sum2)
}
