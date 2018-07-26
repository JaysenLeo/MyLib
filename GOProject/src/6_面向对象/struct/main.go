package main

import "fmt"

type treeNode struct {
	value int
	left, right * treeNode
}
// 给结构体定义打印方法，其中(node treeNode)表示该方法的接受者是那个结构体
func (node treeNode) print()  {
	fmt.Println(node.value)
}

// 给结构体定义设置值方法
func (node *treeNode)  setNode(value int) {
	node.value = value
}

func createNode(val int) *treeNode {
	return &treeNode{ value: val}
}

func main() {

	var root treeNode

	root = treeNode{ value: 3}
	root.left = &treeNode{}
	root.right = &treeNode{5,nil,nil}
	root.right.left = new(treeNode)
	root.left.right = createNode(2)

	root.print()
	root.setNode(1)
	root.print()
	root.left.print()
	root.right.print()
}
