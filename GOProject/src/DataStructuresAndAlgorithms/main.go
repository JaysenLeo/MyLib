package main

import (
	. "./Node"
	. "./SingleLink"
	. "fmt"
)

func main() {
	linkList := CreateLinkList()
	linkList.Add(9)
	linkList.Add(5)
	linkList.Add(2)
	linkList.Add(7)
    linkList.Append(1)
	Println(linkList.IsEmpty())
	Println(linkList.GetLength())
	linkList.Traverse()
	var a *Node
	a = linkList.GetNode(1)
	Println(linkList.Exist(a))
	//var root Node
	//root.SetNode("Lee")
	//root.Next = CreateNode(2)
	//root.Next.Next = CreateNode(3)
	//root.PrintNode()
	//root.Next.PrintNode()
	//fmt.Println(root.GetNextNode())
}
