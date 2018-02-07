class DlLN(object):

    def __init__(self,value,nxt,prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        return  "%s" % self.value

class DLL(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def push(self,obj):
      if self.tail:
          node=DlLN(obj,None,self.tail)
          self.tail.next=node
      else:
          node=DlLN(obj,None,None)
          self.head=node
      self.tail = node



  def pop(self):
      if self.tail == None:
          return None
      elif self.tail == self.head:
          self.tail =None
          node = self.head
          return node.value
      else:
          node = self.tail
          self.tail = node.prev
          return node.value

  def count(self):
    node = self.head
    count =0
    while node:
      count +=1
      node = node.next
    return count

  def unshift(self):
      if self.head:
          node = self.head
          if self.head == self.tail:
              self.head = self.tail =None
          else:
              self.head = node.next
              self.head.prev = None
          return node.value
      else:
          return None

  def detach_mode(self,node):
       curr = self.head
       while curr:
           if curr.value == node.value:
               if curr.prev:
                   if curr.next:
                      curr.prev.next=curr.next
                   else:
                      self.pop()
               else:
                    self.unshift()
               return True
           curr=curr.next
       return False

  def remove(self,obj):
       node=DlLN(obj,self.head,self.tail)
       return self.detach_mode(node)

  def get(self,index):
      node = self.head
      i = 0
      while i != index:
          node = node.next
          i +=1
      if node:
          return node.value
      else:
          return None



def devide(numbers):
      left=DLL()
      right=DLL()
      end = numbers.count()
      mid = numbers.count() / 2
      node = numbers.head
      for i in range(mid):
          left.push(node)
          node = node.next
      for i in range(mid,end):
          right.push(node)
          node = node.next
      return left,right

def merge(left,right):
      result = DLL()
      node1 = left.head
      node2 = right.head
      while node1 or node2:
          if node1 is None or node1.value>node2.value:
              result.push(node2)
              node2 = node2.next
          elif node2 is None or node1.value<node2.value:
              result.push(node1)
              node1=node1.next
      return result
def subsort(numbers):
    p = numbers.head
    mark = p.next
    while mark:
        if mark<p:
            p = mark
            mark = p
        p = p.next
        mark=mark.next
