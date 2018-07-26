package tree

import "fmt"

type Node struct {
	Value       int
	Left, Right *Node
}

func (node Node) Print() {
	fmt.Println(node.Value)
}

func (node *Node) SetNode(value int) {
	if node == nil {
		fmt.Println("Setting Value to nil node. Ignored.")
	}
	node.Value = value
}

func CreateNode(val int) *Node {
	return &Node{Value: val}
}


