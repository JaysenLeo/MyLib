package 协程01

import (
	"time"
	"runtime"
	"fmt"
)

func main()  {


	var a [10]int
	fmt.Println(a)
	for i:= 0; i<10; i++ {
		// 传值，防止闭包，导致index out of range
		go func(j int) {
			for {
				a[j]++
				// 手动交出控制权
				runtime.Gosched()
			}
		}(i)
	}

	time.Sleep(time.Second * 3)
	fmt.Println(a)
}