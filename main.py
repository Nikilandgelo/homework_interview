class Stack():
    
    def __init__(self) -> None:
        self.list_elements = []
    
    def is_empty(self) -> bool:
        if len(self.list_elements) > 0:
            return False
        else:
            return True
    
    def push(self, element) -> None:
        self.list_elements.append(element)

    def pop(self):
        try:
            return self.list_elements.pop()
        except IndexError:
            return "Стэк пуст"
    
    def peek(self):
        try:
            return self.list_elements[-1]
        except IndexError:
            return "Стэк пуст"
    
    def size(self) -> int:
        return len(self.list_elements)


if __name__ == '__main__':
    while True:
        stack = Stack()
        user_input = input("Q - для выхода\nВведите строку со скобками:\n").upper()
        if user_input == 'Q':
            break
        
        for element in list(user_input):
            if element == "}":
                if stack.peek() == "{":
                    stack.pop()
                else:
                    print("Несбалансированно\n")
                    break
            elif element == "]":
                if stack.peek() == "[":
                    stack.pop()
                else:
                    print("Несбалансированно\n")
                    break
            elif element == ")":
                if stack.peek() == "(":
                    stack.pop()
                else:
                    print("Несбалансированно\n")
                    break
            else:
                stack.push(element)
        else:
            if stack.is_empty() == False:
                print(f"Несбалансированно, количество незакрытых скобок {stack.size()}\n")
            else:
                print("Сбалансированно\n")