class TreeNode: # just one node
    def __init__(self, data):
        self.data = data
        self.children = [] # each element of this list be instance of treenode class
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        # self will become parent of child
        child.parent = self # childnode will have parent property, which is set to self
        self.children.append(child)
    
    def print_tree(self):
            
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree()
         

def build_product_tree():
        root = TreeNode("Electronics")


        laptop = TreeNode("Laptop")
        laptop.add_child(TreeNode("Mac"))
        laptop.add_child(TreeNode("Thinkpad"))
        
        cellphone = TreeNode("Cell Phone")
        cellphone.add_child(TreeNode("iPhone"))
        cellphone.add_child(TreeNode("Samsung"))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.print_tree()


if __name__ == '__main__':
    root = build_product_tree()
  