package main

import(
	"fmt"
	"strconv"
	"math/rand"
	"time"
)

type BinTree struct {
	data *int
	parent *BinTree
	left *BinTree
	right *BinTree
}


func createBinTree(parent *BinTree) *BinTree {
	b := BinTree{nil, parent, nil, nil}
	return &b
}


func (b *BinTree) retrieve(key int) (*BinTree) {
	if b.data == nil {
		return b
	} else if key <= *b.data {
		// insert left
		if b.left == nil {
			// no node yet on the left
			b.left = createBinTree(b)
			return b.left
		} else {
			// search further in left
			return b.left.retrieve(key)
		}
	} else if key > *b.data {
		// insert right
		if b.right == nil {
			// no node yet
			b.right = createBinTree(b)
			return b.right
		} else {
			// search further right
			return b.right.retrieve(key)
		}
	}
	return b
}

func (b *BinTree) to_string() (s string) {
	if b != nil && b.data != nil {
		s += strconv.Itoa(*b.data)
		s += " [" + b.left.to_string() + " " + b.right.to_string() + "]"
	} else {
		s = "/"
	}
	return
}


func (b *BinTree) inorder_succ() *BinTree {
	if b == nil { return nil }
	
	if b.right == nil { return nil }
	
	return b.right.mostleft()
}


func (b *BinTree) mostleft() *BinTree {
	if b == nil { return nil }
	
	if b.left == nil {
		return b
	} else {
		return b.left.mostleft()
	}
}


func (b *BinTree) insert(data int) {
	where := b.retrieve(data)
	*where = *createBinTree(where.parent)
	(*where).data = &data
}

func (b *BinTree) height(i int) int {
	if b == nil { return i }
	
	return max(b.left.height(i+1), b.right.height(i+1))
}


// Helpers

func max(a,b int) int {
	if a<b { return b }
	return a
}


func sum(m []int) int {
	total := 0
	for i:=0; i<len(m); i++ {
		total += m[i]
	}
	return total
}

/*
func (b *BinTree) del(data int) {
	where := b.retrieve(data)
	parent := where.parent
	
	if where.left == nil && where.right == nil {
		// just delete
		// .................
		
}
*/

func test(result chan<- float64, num_elements, iter int) {
	//fmt.Println("Hi I'm a worker!")
	
	//time.Sleep(time.Second * 5)
	//result <- 10
	
	result <- _test(num_elements, iter)
}

func _test(num_elements, iter int) float64 {
	source := rand.NewSource(time.Now().UnixNano())
    generator := rand.New(source)
	
	results := make([]int, iter)
	for run := 0; run < iter; run++ {
		perm := generator.Perm(num_elements)
		
		b := createBinTree(nil)
		for i, _ := range(perm) {
			b.insert(i)
		}
		
		results[run] = b.height(0)
	}
	return float64(sum(results))/float64(iter)
}


func main() {
	/*
	b := createBinTree(nil)
	for _, i := range([]int{100, 50, 20, 10, 30, 70, 60, 80, 150, 120, 110, 130, 170, 160, 180}) {
		b.insert(i)
		fmt.Println(i, "||", b.to_string())
	}
	//fmt.Println(*b.retrieve(100).inorder_succ().data)
	fmt.Println(b.to_string())
	fmt.Println(b.height(0))
	b.insert(987)
	fmt.Println(b.height(0))
	*/
	
	
	workers := 8
	
	fmt.Print("{")
	j := 1
	for i:=0; i<9; i+=1 {
		j+=i+j+1
		
		averages := make(chan float64, workers)
		
		for k:=0; k<workers; k++ {
			go test(averages, j, 2000)
		}
		
		total := 0.0
		for k:=0; k<workers; k++ {
			total += <-averages
		}
		
		h := total/float64(workers)
		
		fmt.Print("{")
		fmt.Print(j)
		fmt.Print(", ")
		fmt.Print(h,"},\n")
	}
	fmt.Print("}\n")
}


//EOF