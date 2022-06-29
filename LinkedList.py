listLength = 10

#Using 2 arrays
data = [-1] * listLength
nextNode = [i+1 for i in range(listLength-1)] + [-1]
startPointer = 0
emptyList = 0

def outputNodes():
    global data, nextNode, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Linked list is empty')
        return False
    while pointer != -1:
        print(data[pointer])
        pointer = nextNode[pointer]
    return True

def addNode(element):
    global data, nextNode, startPointer, emptyList
    if emptyList == -1:
        print('Linked list is full')
        return False
    pointer = startPointer
    if pointer != emptyList:
        while nextNode[pointer] != -1:
            pointer = nextNode[pointer]
        nextNode[pointer] = emptyList
        pointer = emptyList
    emptyList = nextNode[pointer]
    data[pointer] = element
    nextNode[pointer] = -1
    return True

def popNode():
    global data, nextNode, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Linked list is empty')
        return False
    prevNode = pointer
    while nextNode[pointer] != -1:
        prevNode = pointer
        pointer = nextNode[pointer]
    if prevNode != pointer:
        nextNode[prevNode] = -1
    nextNode[pointer] = emptyList
    emptyList = pointer
    return data[pointer]

def delNode(element):
    global data, nextNode, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Linked list is empty')
        return False
    prevNode = pointer
    while nextNode[pointer] != -1:
        if data[pointer] == element:
            break
        prevNode = pointer
        pointer = nextNode[pointer]
    else:
        print('Element not found in list')
        return False
    if prevNode != pointer:
        nextNode[prevNode] = nextNode[pointer]
    else:
        startPointer = nextNode[prevNode]
    nextNode[pointer] = emptyList
    emptyList = pointer
    return True

#Using classes
class node:
    def __init__(self,data,nextNode):
        self.data = data
        self.nextNode = nextNode
linkedList = [node(-1,i+1) for i in range(listLength-1)] + [node(-1,-1)]
startPointer = 0
emptyList = 0

def outputNodes():
    global linkedList, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Linked list is empty')
        return False
    while pointer != -1:
        print(linkedList[pointer].data)
        pointer = linkedList[pointer].nextNode
    return True

def addNode(element):
    global linkedList, startPointer, emptyList
    if emptyList == -1:
        print('Linked list is full')
        return False
    pointer = startPointer
    if pointer != emptyList:
        while linkedList[pointer].nextNode != -1:
            pointer = linkedList[pointer].nextNode
        linkedList[pointer].nextNode = emptyList
        pointer = emptyList
    emptyList = linkedList[pointer].nextNode
    linkedList[pointer].data = element
    linkedList[pointer].nextNode = -1
    return True

def popNode():
    global data, nextNode, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Linked list is empty')
        return False
    prevNode = pointer
    while linkedList[pointer].nextNode != -1:
        prevNode = pointer
        pointer = linkedList[pointer].nextNode
    if prevNode != pointer:
        linkedList[prevNode].nextNode = -1
    linkedList[pointer].nextNode = emptyList
    emptyList = pointer
    return linkedList[pointer].data

def delNode(element):
    global linkedList, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Linked list is empty')
        return False
    prevNode = pointer
    while linkedList[pointer].nextNode != -1:
        if linkedList[pointer].data == element:
            break
        prevNode = pointer
        pointer = linkedList[pointer].nextNode
    else:
        print('Element not found in list')
        return False
    if prevNode != pointer:
        linkedList[prevNode].nextNode = linkedList[pointer].nextNode
    else:
        startPointer = linkedList[prevNode].nextNode
    linkedList[pointer].nextNode = emptyList
    emptyList = pointer
    return True