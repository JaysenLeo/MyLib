package SingleLink

import (
	. "../Node"
	"fmt"
)

// 链表
type LinkList struct {
	head *Node
	tail *Node
	size int
}

//新建空链表，即创建Node指针head，用来指向链表第一个结点，初始为空
func CreateLinkList() LinkList{
	Link:=LinkList{}
	Link.head=nil //head指向头部结点
	Link.tail=nil //tail指向尾部结点
	Link.size=0
	return Link
}

//检查是否为空链表
func(link *LinkList) IsEmpty() bool{
	return link.size==0
}

//获取链表长度
func(link *LinkList) GetLength() int{
	return link.size
}

// 从链表尾部添加数据
func(link *LinkList) Append(value interface{}) {
	newNode := Node{}
	newNode.Value = value
	newNode.Next = nil

	if (link.size == 0){
		link.head = &newNode
		link.tail = &newNode
	} else {
		link.tail.Next = &newNode
		link.tail = &newNode

	}
	link.size ++
}

//在链表头部插入数据
func(link *LinkList) Add(value interface{}){
	newNode:=Node{}
	newNode.Value = value
	newNode.Next = link.head
	link.head = &newNode
	if(link.size == 0){
		link.tail = &newNode
	}
	link.size++
}

//是否含有指定结点
func(link *LinkList) Exist(node *Node) bool{
	var p *Node=link.head
	for p!=nil{
		if(p==node){
			return true
		}else{
			p=p.Next
		}
	}
	return false
}

//获取含有指定数据的第一个结点
func(link *LinkList) GetNode(value interface{}) *Node{
	var p *Node=link.head
	for p!=nil{
		//找到该数据所在结点
		if value == p.Value{
			return p
		}else{
			p=p.Next
		}
	}
	return nil
}

//在指定结点后面插入数据
func(link *LinkList) InsertAfterNode(pre *Node,value interface{}){
	//如果链表中存在该结点，才进行插入
	if link.Exist(pre){
		newNode:=Node{}
		newNode.Value=value
		if(pre.Next==nil){
			link.Append(value)
		}else{
			newNode.Next=pre.Next
			pre.Next=&newNode
		}
		link.size++
	}else{
		fmt.Println("链表中不存在该结点")
	}
}

//在第一次出现指定数据的结点后插入数据,若链表中无该数据，返回false
func(link *LinkList) InsertAfterData(preData interface{},value interface{}) bool{
	var p *Node=link.head
	for p != nil{
		//找到该数据所在结点
		if p.Value == preData{
			link.InsertAfterNode(p ,value)
			return true
		}else{
			p = p.Next
		}
	}
	//没有找到该数据
	fmt.Println("链表中没有该数据，插入失败")
	return false
}

//在指定下标处插入数据
func(link *LinkList) Insert(position int,e interface{}) bool{
	if position < 0{
		fmt.Println("指定下标不合法")
		return false
	}else if position == 0{
		//在头部插入
		link.Add(e)
		return true
	}else if position == link.size{
		//在尾部插入
		link.Append(e)
		return true
	}else if position > link.size{
		fmt.Println("指定下标超出链表长度")
		return false
	}else{
		//在中间插入
		var index int
		var p *Node=link.head
		//逐个移动指针
		//position是插入后新结点的下标，position-1时需要定位到的其前一个结点的下标
		for index=0; index < position-1; index++{
			p=p.Next
		}
		//找到
		link.InsertAfterNode(p,e)
		return true
	}

}

//删除第一个含指定数据的结点
func(link *LinkList) DeleteSomeNode(e interface{}){
	p := link.GetNode(e)
	if p == nil{
		fmt.Println("链表中无该数据，删除失败")
	}else{
		link.DeleteNode(p)
	}
}

//删除指定结点
func(link *LinkList) DeleteNode(node *Node){
	//存在该结点
	if link.Exist(node){
		//若 node 是头部结点
		if node == link.head{
			link.head = link.head.Next
		//若 node 是尾部结点
		}else if node == link.tail{
			//寻找为节点的前一个结点的指针
			var p *Node = link.head
			for p.Next != link.tail{
				p = p.Next
			}
			// 倒数第二个节点
			p.Next = nil
			// 倒数第二个结点成为最后一个节点
			link.tail = p
		//node是中间结点
		}else{
			var p *Node=link.head
			for p.Next!=node{
				p=p.Next
			}
			// 把要删除的node覆盖掉
			p.Next=node.Next
		}
		link.size--
	}
}

// 遍历
func(link *LinkList) Traverse() {

	var p *Node = link.head
	if(link.IsEmpty()){
		fmt.Println("LinkList is empty")
	}else{
		for p!=nil{
			fmt.Print(p.Value," ")
			p=p.Next
		}
		fmt.Println()
	}
}

