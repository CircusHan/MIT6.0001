# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2,Node(1),Node(6)), Node(10)) #TODO
tree2 = Node(7, Node(2,Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10))) #TODO
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))) #TODO

def find_tree_height(tree : Node):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    #Base condition.
    if tree is None :
        return 0
    if tree.get_right_child() == None and tree.get_left_child() == None:
        return 0
    else:
        left_height = find_tree_height(tree.get_left_child())
        right_height = find_tree_height(tree.get_right_child())
        return max(left_height, right_height) + 1


def is_heap(tree: Node,compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    if tree is None :
        return True

    if tree.get_left_child() == None:
        is_left_heap = True
        left_compare = True
    else:
        is_left_heap = is_heap(tree.get_left_child(), compare_func)
        left_compare = compare_func(tree.get_left_child().value, tree.value)

    if tree.get_right_child() == None:
        is_right_heap = True
        right_compare = True
    else:
        is_right_heap = is_heap(tree.get_right_child(), compare_func)
        right_compare = compare_func(tree.get_right_child().value, tree.value)

    return is_left_heap and is_right_heap and left_compare and right_compare





if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
