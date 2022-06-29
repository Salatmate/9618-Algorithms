listLength = 10
stack = [None] * listLength
pointer = 0

def push(element):
    global stack, pointer, listLength
    if pointer >= listLength:
        print('List is full')
        return False
    stack[pointer] = element
    pointer += 1
    return True

def pop():
    global stack, pointer, listLength
    if pointer == 0:
        print('List is empty')
        return False
    pointer -= 1
    return stack[pointer]