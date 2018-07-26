package 协程01

import "fmt"

func sum(s []int, result chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	result <- sum
}

func main() {
	s := []int{1, 4, -5, 7, 10, 2, 1, 10}
	res := make(chan int)
	go sum(s[:len(s)/2], res)
	go sum(s[len(s)/2:], res)
	x, y := <-res, <-res

	fmt.Println(x, y, x+y)
}
