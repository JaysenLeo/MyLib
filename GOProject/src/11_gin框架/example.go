package main

import (
	"github.com/gin-gonic/gin"
	"fmt"
)

type LoggingParams struct {
	ThreadName string `json:"thread_name" binding:"required"`
	ServiceName string `json:"service_name" binding:"required"`
	// HandleName string `json:"handle_name" binding:"required"`
	// MethodName string `json:"handle_name" binding:"required"`
	// FunctionName string `json:"handle_name" binding:"required"`
	// ClassName string `json:"class_name" binding:"required"`
}

func main() {
	router := gin.Default()
	router.POST("/logging", test)
	router.Run(":8001") // listen and serve on 0.0.0.0:8080
}

func test(c *gin.Context) {
	var log LoggingParams
	//buf := make([]byte, 1024)
	//n, _ := c.Request.Body.Read(buf)
	//fmt.Println(string(buf[0:n]))
	e := c.BindJSON(&log)
	fmt.Println(e)
	//fmt.Println(c.DefaultPostForm("thread_name", "anonymous"))
	c.JSON(200, gin.H{
		"threadName": log.ThreadName,
		"serviceName": log.ServiceName,
	})
}
