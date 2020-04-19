### 3.1. Describe how you could use a single aray to implement three stacks.



# The first three cells of the self.items list hold the index of the top item in each stack.
# The cells after that hold stacks data. 
# We need to have a history of the members in each stack. So every time we add an item to a stack, 
# we also record the index of the last member of that stack.
# So items are added in pairs. E.g. if we want to add number 5 to the stack two, and index of the
# top item of that stack was 7, we add the pair (5, 7)

class threeStack:
  def __init__(self):
    self.items = [None, None, None]  
  

  def isEmpty(self, stack_num):
    assert stack_num in [1, 2, 3]
    return self.items[stack_num - 1] is None


  def update_indeces(self, starting_index):
    # when we delete an item, we need to update the indeces that appear as the second element of pairs
    # and also update values of the first three cells of self.items
    for item in self.items[starting_index:]:
      if item[1] and item[1] > starting_index:
        item[1] -= 1
    for index, item in enumerate(self.items[:3]):
      if item and item > starting_index:
        self.items[index] -= 1


  def push(self, stack_num, item):
    
    self.items.append( [ item, self.items[stack_num - 1] ] )

    # recording the index of the top item of the given stack
    self.items[stack_num - 1] = len(self.items) - 1


  def pop(self, stack_num):
    
    assert stack_num in [1, 2 , 3]

    # getting the index of top pair in the given stack and the pair itself
    top_pair_idx = self.items[stack_num - 1]
    cur_top_pair = self.items[top_pair_idx]

    # change the pointer to the new top item
    self.items[stack_num - 1] = cur_top_pair[1]

    # deletting the item at the given index
    del self.items[top_pair_idx]

    # updating indeces
    self.update_indeces(starting_index=top_pair_idx)


  def print_stack(self, stack_num):
    output = []
    top_index = self.items[ stack_num - 1 ]
    while top_index:
      val, prev_index = self.items[top_index]
      output.append(val)
      top_index = prev_index
    print(output[::-1])
  
  
  def __str__(self):
    return str(self.items)
  


a = threeStack()
a.push(1, 10)
a.push(1, 12)
a.push(1, 15)
a.push(2, 25)
a.push(3, 37)
a.push(2, 24)
a.push(3, 33)
a.print_stack(1)
a.print_stack(2)
a.print_stack(3)
print(a)
a.pop(1)
print(a)
a.pop(1)
print(a)
a.pop(1)
print(a)
a.pop(3)
print(a)
a.print_stack(1)
a.print_stack(2)
a.print_stack(3)
