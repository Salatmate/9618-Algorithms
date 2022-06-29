listLength = 10

#Using 3 arrays
data = [-1] * listLength
leftNode = [-1] * listLength
rightNode = [-1] * listLength
startPointer = 0
emptyList = 0

def checkNode(element):
    global data, leftNode, rightNode, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Binary tree is empty')
        return False
    while pointer != -1:
        if element == data[pointer]:
            print('Element is found')
            return True
        elif element < data[pointer]:
            pointer = leftNode[pointer]
        else:
            pointer = rightNode[pointer]
    print('Element is not found')
    return False

def addNode(element):
    global data, leftNode, rightNode, startPointer, emptyList
    pointer = startPointer
    if emptyList >= len(data):
        print('Binary tree is full')
        return False
    if pointer != emptyList:
        while pointer != -1:
            prevNode = pointer
            if element < data[pointer]:
                pointer = leftNode[pointer]
            else:
                pointer = rightNode[pointer]
        if element < data[prevNode]:
            leftNode[prevNode] = emptyList
        else:
            rightNode[prevNode] = emptyList
    data[emptyList] = element
    emptyList += 1
    return True

#Using classes
class node:
    def __init__(self,data,leftNode,rightNode):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode

tree = [node(-1,-1,-1)] * listLength
startPointer = 0
emptyList = 0

def checkNode(element):
    global tree, startPointer, emptyList
    pointer = startPointer
    if pointer == emptyList:
        print('Binary tree is empty')
        return False
    while pointer != -1:
        if element == tree[pointer].data:
            print('Element is found')
            return True
        elif element < tree[pointer].data:
            pointer = tree[pointer].leftNode
        else:
            pointer = tree[pointer].rightNode
    print('Element is not found')
    return False

def addNode(element):
    global tree, startPointer, emptyList
    pointer = startPointer
    if emptyList >= len(tree):
        print('Binary tree is full')
        return False
    if pointer != emptyList:
        while pointer != -1:
            prevNode = pointer
            if element < tree[pointer].data:
                pointer = tree[pointer].leftNode
            else:
                pointer = tree[pointer].rightNode
        if element < tree[prevNode].data:
            tree[prevNode].leftNode = emptyList
        else:
            tree[prevNode].rightNode = emptyList
    tree[emptyList].data = element
    emptyList += 1
    return True