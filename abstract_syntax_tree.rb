require "json"
require "awesome_print"
require 'pry'

valid_inputs = [
  "id",
  "id,post_title",
  "id,post_title,comments(message)",
  "id,post_title,comments(message,created_at)",
  "id,post_title,comments(message,created_at,author(id,name))",
  "id,post_title,comments(message,created_at,author(id,name)),tags(id,name)",
  "tags(id,name),id,post_title,comments(message,created_at,author(id,name))",
  "2093840sasf9i93i945923KSD(S#$(029rweoprfjsdjfjsdf012ekkm%,32490234903(03204)",
  "id,post_title,comments(id,message,author(id,name,profile(id,dob)))"
]

invalid_inputs = [
  "id,post_title,comments("
]


class Parser
  # MAX_INPUT_LENGTH, MAX_FIELDS_SIZE, and MAX_DEPTH_SIZE are defined for security reasons.
  # DESC: Prevent attacks where a user can pass lengthy strings in the field and we waste a lot of memory parsing it.
  MAX_INPUT_LENGTH = 1500

  # DESC: To have reasonable limits to prevent any possible attacks.
  MAX_FIELDS_SIZE = 50

  # DESC: Maximum nesting allowed. This is to prevent attackers from increasing our memory usage by passing a lot of fields
  #   with length 1 and nested them as much as they can.
  MAX_DEPTH_SIZE = 10

  def self.parse(string)
    if string.length > MAX_INPUT_LENGTH
      raise ParserError, "Maximum input length should not be more than #{MAX_INPUT_LENGTH}"
    end

    # DESC:
    #   This is the base data structure being returned.
    #   In case, if the input string is empty, this is the value that will be returned.
    #   Types can be:
    #     1. `root` (base node): Indicates the root of the tree. Not used for anything else.
    #     2. `simple`: Indicates the simple field.
    #     3. `relationship`: Indicates a relationship that will have nested fields.
    tree = {
      type: :root,
      fields: []
    }

    # DESC:
    #   Stack keeps track of the nesting we're currently in.
    #   It contains pointers to the "fields" list of any node in the tree, starting at the "fields" list of the root node.
    #   Whenever we encounter a "(" (nested field) in the input, we add the new node's "fields" list to the stack. Future fields will now be added to this new node (nested fields).
    #   Whenever we encounter a ")", we pop that node from the stack so that newer fields get added to the parent node.
    stack = [tree[:fields]]
    current_position = 0

    # ALGORITHM:
    #   We parse fields in the following way:
    #     When we encounter any alphabet or underscore, we add it to the current character buffer.
    #     If we encounter a `,`, then it marks the end of the previous field, and we add the current field to the top of the stack.
    #     If we encounter a `(`, then we again add the current field to the top of the stack, but push it to the stack so that new fields now get added to this new node.
    #     If we encounter a `)`, then we add the current field to the top of the stack, but the pop the stack. Pop marks the end of a node in the tree.
    #   Iterating over the characters 1 more than its length to validate the syntax and count of nodes in the stack. In the end, if more than a root element exists in th stack, we encountered syntax error.
    for cursor in 0..string.length
      case string[cursor]
      when ","
        node_value = string[current_position...cursor].strip

        if node_value.length > MAX_FIELDS_SIZE
          raise ParserError, "Maximum fields size should not be more than #{MAX_FIELDS_SIZE}"
        end
        
        # DESC:
        #   Prevents bad field names if we encounter successive commas like "id,,title".
        if node_value != ""
          node =  {
            type: :simple,
            name: node_value
          }

          stack.last << node
        end

        current_position = cursor + 1
      when "("
        node_value = string[current_position...cursor].strip

        if stack.length >= MAX_DEPTH_SIZE
          raise ParserError, "Maximum depth size should not be more than #{MAX_DEPTH_SIZE}"
        end

        if node_value != ""
          node = {
            type: :relationship,
            name: node_value,
            fields: []
          }
          stack.last << node
          stack << node[:fields]
        end

        current_position = cursor + 1
      when ")"
        node_value = string[current_position...cursor].strip
        if node_value != ""
          node = {
            type: :simple,
            name: node_value
          }
          stack.last << node
        end

        # DESC:
        #   If in case, iterator is trying to pop the root field, then there must be some issues with the fields listed (probably, syntactical).
        if stack.length == 1
          raise ParserError, "Trying to remove the root node. Check the syntax"
        else
          stack.pop
        end

        current_position = cursor + 1
      when nil
        # DESC:
        #   At the end of string, if there are more than a root element in the stack, then we encountered syntax error.
        if cursor == string.length && stack.length > 1
          raise ParserError, "Parentheses were not closed. Parser detected the syntax error"
        end
      else
        if cursor == (string.length - 1)
          # DESC:
          #   At the end of string, of stack holds more than 1 element, then we have encountered syntax error.
          if stack.length > 1
            raise ParserError, "Parentheses were not closed. Parser detected the syntax error"
          end

          node_value = string[current_position..cursor].strip

          if node_value.length > MAX_FIELDS_SIZE
            raise ParserError, "Maximum fields size should not be more than #{MAX_FIELDS_SIZE}"
          end

          node = {
            type: :simple,
            name: node_value
          }
          stack.last << node
        end
      end
    end

    return tree
  end
end

class ParserError < StandardError
end

valid_inputs.each do |i|
  p Parser.parse(i)
end

# OUTPUTS:
#
#
# {
#   :type => :root,
#   :fields => [
#     [0] {
#       :type => :simple,
#       :name => "id"
#     },
#     [1] {
#       :type => :simple,
#       :name => "post_title"
#     },
#     [2] {
#       :type => :relationship,
#       :name => "comments",
#       :fields => [
#         [0] {
#           :type => :simple,
#           :name => "message"
#         }
#       ]
#     }
#   ]
# }
#
#

invalid_inputs.each do |i|
  Parser.parse(i)
end

# OUTPUTS:
# Throws:
# /Users/kavitakanojiya/Desktop/parser_ex.rb:128:in `block in parse': Parentheses were not closed. Parser detected the syntax error (ParserError)
#
#
