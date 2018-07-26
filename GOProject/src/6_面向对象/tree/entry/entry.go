package main

import (
	. "../../tree"
	)

func main() {
	//var root Node
	//fmt.Println(root)
	//// 构造一个简单的树
	//root = Node{ value:3}
	//root.left = &Node{ }
	//root.right = &Node{ 5,nil,nil }
	//root.right.left = new(Node)
	//root.right.right = createNode(2)
	//
	////	切片中定义
	//nodes := []Node {
	//{value: 3},
	//	{value: 4},
	//	{5,nil,&root},
	//}
	//fmt.Println(nodes)
	// ------------------------
	var root Node

	root = Node{  Value:3}
	root.Left = &Node{}
	root.Right = &Node{5, nil, nil}
	root.Right.Left = new(Node)
	root.Right.Left.SetNode(4)
	root.Left.Right = CreateNode(2)

	root.Traverse()
}