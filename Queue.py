listLength = 10
queue = [None] * listLength
startPointer = 0
rearPointer = 1

def enqueue(element):
    global queue, startPointer, rearPointer, listLength
    if startPointer == rearPointer:
        print('List is full')
        return False
    queue[rearPointer] = element
    rearPointer = (rearPointer + 1) % listLength
    return True

def dequeue():
    global queue, startPointer, rearPointer, listLength
    if startPointer + 1 == rearPointer:
        print('List is empty')
        return False
    startPointer = (startPointer + 1) % listLength
    return queue[startPointer]