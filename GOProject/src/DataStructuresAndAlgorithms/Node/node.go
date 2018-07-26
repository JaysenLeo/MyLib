package Node

import (
	"fmt"
)

// 节点
type Node struct {
	Value interface{}
	Next  *Node
}



// 打印节点的数据域
func (node Node) PrintNode() {
	fmt.Println(node.Value)
}

// 获取节点的数据域
func (node *Node) GetNode() interface{} {
	return node.Value
}

// 获取节点的下一个节点
func (node *Node) GetNextNode() *Node {
	return node.Next
}

// 设置节点的数据域
func (node *Node) SetNode(value interface{}) {
	node.Value = value
}

// 设置节点的下一个节点
func (node *Node) SetNextNode(nextNode *Node) {
	node.Next = nextNode
}

func CreateNode(val interface{}) *Node {
	return &Node{Value: val}
}
