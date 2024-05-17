### Basic Types
```go
int
uint
float
char
bool
str
```

### Numbers
```go
int8
int16
int32
int64
int128
int256
```

### Array
```go
[1, 2, 3]

int[3]

x[3] -> returns value
```

### Functon
```go
const foo: int(int, int) = (const x: int, const y: int){
    return x + y + 1
}
foo(1, 2) 
```

### Map
```go
bool{int}
{1: true, 4: false}
x[3] -> returns value of bool
```


### Pointers/References
```go
// if structs are with keyword before varaible
var x: int = 3 
ref r: int = x // maybe if does not create pointer 

// s

&v -> returns the pointer
var p: *int = &v
p -> pointer address
*p -> the derefrenced value

new() -> returns pointer of something aloocated to heap 
delete() -> deletes varialbe in heap
```


### Structs
```go

const LinkedList: type = {
    const Node: type = {
        var x: int = 3;
        var next: *Node = null; 
    } 
    var head: Item = Item();
    
    
    const append: (int) = (const value: int){
        const new_node: *Node = new(Node(value))

        if (head == null) {
            head = new_node;
        } else {
            var current_node: *Node = head;
            while (current_node != null) {
                current_node = current_node.next
            } else {
                &current_node.next = new_node;
            }
        }
    }

    const pop: (int) = (const index: int){
        var current_node: *Node = head;
        while (current_node.next.next != null) {
            current_node = current_node.next;
        } else {
            delete(current_node.next);
            &current_node.next = null;
        }
    }a

}

```
// maybe look into having something where
// the reference goes and you cna then use & to get poiner 





var foo: int(int, int) = (const x: int, const y: int){
    return x + y;
};
const arr: int[3] = [1, 2, 3];
var p: &int = m;


const str type = char[]
var arr: int[] = [1, 2, 3];
arr = [1, 2, 4, 5] // ERROR


but this works
var arr: int[] = [1, 2, 3, 4];
// so as parameter and returing
yay

refereces like rust
so

// because reference != pointer
// reference does not pointer in meomety
ref x int = y

// for heap pontes must be ref
ref h int = &new(3


also for variables of class like &foo.leafs gives pointer to leafs and if it i have pointer to foo if i get pointer_foo.leafs is give pointer
also even though ref doesnet always create pointer in stack as compiler just replaces it sometimes in thsi code have it do that

this is main file

OR COULD HAVE REFERENCE TYPE that is like &varitable 
LOOK AT HOW const are declared while runtime and also think about looking on struts and how to make them

POINTER METHOD WORKS AND IS GOOD BUT WE COULD LOOK INTO REFS
delete() and new() both work well 
const declared during run time are added to stack
so having var and const inside of a struct works
look into struct constructor though 
