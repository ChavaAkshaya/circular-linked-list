class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createCLL(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            newNode=Node(val)
            newNode.prev=temp
            temp.next=newNode
            temp=temp.next
    temp.next=head
    head.prev=temp
    printdll(head)
def printdll(head):
    temp=head
    while(temp):
        print(temp.prev,temp.data,temp.next)
        print()
        temp=temp.next
arr=list(map(int,input().split()))
print( createCLL(arr))