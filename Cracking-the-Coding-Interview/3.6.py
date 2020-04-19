#  3.6 An animal shelter, which holds only dogs and cats, operates on a
#  strictly"first in, first out"basis. People must adopt either
#  the"oldest"(based on arrival time) of all animals at the shelter, or they can
#  select whether they would prefer a dog or a cat (and will receive the oldest
#  animal of that type). They cannot select which specific animal they would
#  like. Create the data structures to maintain this system and implement
#  operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may
#  use the built in Linked list data structure.

class Animal:
  def __init__(self, name, a_type, id):
    self.name = name
    self.type = a_type
    self.id = id

class AnimalQ:

  def __init__(self):
    self.animal_id = 1
    self.cat_q = Queue()  # assuming we have defined a class Queue()
    self.dog_q = Queue()


  def enQ(self, name, animal_type):
    assert animal_type in ['cat', 'dog']
    n = Animal(name, animal_type, self.animal_id)
    if n.type == 'cat':
      self.cat_q.enqueue(n)
    else:
      self.dog_q.enqueue(n)
    self.animal_id += 1


  def deQ_cat(self):
    return self.cat_q.dequque()
  

  def deQ_dog(self):
    return  self.dog_q.dequque()


  def deQ_any(self):
    c = self.cat_q.peek()
    d = self.dog_q.peek()
    return c if c.id < d.id else d

a = AnimalQ()
a.enQ('a_1', 'cat')
a.enQ('b_2', 'cat')
a.enQ('c_3', 'dog')
a.enQ('d_4', 'dog')
a.enQ('e_5', 'cat')
print(a.deQ_cat().name)
print(a.deQ_dog().name)
print(a.deQ_any().name)
