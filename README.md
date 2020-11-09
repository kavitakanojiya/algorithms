# Singly Linked List

```ruby
node_1 = Node.new(node: 'Hello')
node_2 = Node.new(node: 'Kavita')
node_3 = Node.new(node: 'Pleasant')
node_4 = Node.new(node: 'morning')

node_1.add(element: node_2)
node_2.add(element: node_3)
node_3.add(element: node_4)

# 1 to 3rd position
p "Positioning `1` to position 3"
sll = SinglyLinkedList.new(nodes: [1,2,3,4,5])
list = sll.virtual_list
element = list[0]
position = 3
sll.insert_after(element: element, position: position)
p sll.list

OUTPUT:
"Positioning `1` to position 3"

#<Node:0x007f86c6163290 @current_node=2, @next=#<Node:0x007f86c6163218 @current_node=3, @next=#<Node:0x007f86c6162f98 @current_node=1, @next=#<Node:0x007f86c61631a0 @current_node=4, @next=#<Node:0x007f86c6163128 @current_node=5, @next=nil, @previous=nil>, @previous=nil>, @previous=nil>, @previous=nil>, @previous=nil>
```


# Binary Conversion
```ruby
BinaryConversion::StartWith0.new(number: 9).convert

OUTPUT:
[1, 0, 0, 1]
```


```ruby
BinaryConversion::StartWith0.new(number: 100).convert

OUTPUT:
[1, 0, 0, 1]
```
