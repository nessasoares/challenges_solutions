class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items


def convert_int_to_bin(dec_num):
  can_divide = True
  stack = Stack()
  num = dec_num

  while can_divide:
    rest = int(num % 2)
    num = num // 2

    stack.push(str(rest))

    if num == 0:
      can_divide = False

  return get_binary_number(stack.get_stack())
  
def get_binary_number(stack):
  return ''.join(stack[::-1])

if __name__ == '__main__':
    number = int(input())
    converted = convert_int_to_bin(number)

    print(converted)