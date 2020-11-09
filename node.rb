require 'pry'

class Node
  attr_accessor :current_node, :next, :previous

  def initialize(node:)
    @current_node = node
    @next = nil
    @previous = nil
  end

  def add(element:)
    @next = element
    element.previous = self
  end
end

class SinglyLinkedList
  attr_accessor :nodes, :head, :tail, :list
  def initialize(nodes:)
    @nodes = nodes
    @head = @tail = nil
    @list = self.generate_list
  end

  def virtual_list
    nodes.map do |node|
      Node.new(node: node)
    end
  end

  def generate_list
    _list = self.virtual_list

    @head = _list.first.dup

    @tail = _list.last

    _list.each_with_index do |node, i|
      node.next = _list[i+1]
    end

    _list.first
  end

  def remove(node:)
    expected_node = @list
    previous = nil

    while true
      if expected_node.current_node == node.current_node
        if previous
          previous.next = expected_node.next
        else
          @list = expected_node.next
        end
        break
      end
      previous = expected_node
      expected_node = expected_node.next
    end
  end

  # shuffle
  def insert_after(element:, position:)
    # remove element from the linked list
    remove(node: element)

    # since we want to push element ahead of this position
    position -= 1

    expected_node = @list

    current_position = 1

    while true
      if current_position == position
        element.next = expected_node.next
        expected_node.next = element
        break
      end
      current_position += 1

      if expected_node.next.nil?
        element.next = @list
        @list = element
        break
      end
      expected_node = expected_node.next
    end
  end
end

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

# moved to 4th position
p "Positioning `2` to position 4"
sll = SinglyLinkedList.new(nodes: [1,2,3,4,5])
list = sll.virtual_list
element = list[1]
position = 4
sll.insert_after(element: element, position: position)
p sll.list

# 4 moved to 3rd position
p 'Positioning `4` to position 3'
sll = SinglyLinkedList.new(nodes: [1,2,3,4,5])
list = sll.virtual_list
element = list[3]
position = 3
sll.insert_after(element: element, position: position)
p sll.list


# 4 moved to 3rd position
p 'Positioning `5` to position 1'
sll = SinglyLinkedList.new(nodes: [1,2,3,4,5])
list = sll.virtual_list
element = list[4]
position = 1
sll.insert_after(element: element, position: position)
p sll.list
