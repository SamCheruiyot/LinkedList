from enum import nonmember



class linkedlistsNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

node1=linkedlistsNode("1")
node2=linkedlistsNode("2")
node3=linkedlistsNode("3")
node4=linkedlistsNode("4")
node5=linkedlistsNode("5")
node6=linkedlistsNode("6")
node7=linkedlistsNode("7")
node8=linkedlistsNode("8")

node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4
node4.nextNode=node5
node5.nextNode=node6

currentNode=node1

while True:
    print(currentNode.value,">>>",end=" ")

    if currentNode.nextNode is None:
        print("None")
        break

    currentNode=currentNode.nextNode


