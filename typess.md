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
    }

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
// so can have array of unknow length as parameter and returing beacuse it is added to the stack top
yay

refereces like rust
so

// because reference != pointer
// reference does not pointer in meomety
ref x int = y

// for heap pontes
ref h int = &new(3)
