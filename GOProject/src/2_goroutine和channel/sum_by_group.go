package main

import "fmt"

func sum(a []int, result chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	result <- sum
}

func main() {
	a := []int{2, 3, 5, 6, 10, -5, 1, 0}
	result := make(chan int)
	go sum(a[:len(a)/2], result) /* 此处 不阻塞 当即返回执行 下面的代码 执行中产生的结果 放入管道 result中 */
	go sum(a[len(a)/2:], result)
	x, y := <-result, <-result

	fmt.Println(x, y, x+y)
}
