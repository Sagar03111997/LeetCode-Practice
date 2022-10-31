class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode


    def push_at(self, newElement, position):
        newNode = Node(newElement)
        if(position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("\nThe previous node is null.")

    def mergeLists(headA, headB):

        # A dummy node to store the result
        dummyNode = Node(0)

        # Tail stores the last node
        tail = dummyNode
        while True:

            # If any of the list gets completely empty
            # directly join all the elements of the other list
            if headA is None:
                tail.next = headB
                break
            if headB is None:
                tail.next = headA
                break

            # Compare the data of the lists and whichever is smaller is
            # appended to the last of the merged list and the head is changed
            if headA.data <= headB.data:
                tail.next = headA
                headA = headA.next
            else:
                tail.next = headB
                headB = headB.next

            # Advance the tail
            tail = tail.next

        # Returns the head of the merged list
        return dummyNode.next

    def PrintList(self):
        temp = self.head
        if(temp != None):
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                # Data found
                return True
            current = current.next
        return  False


    def update(self, x, y):
        current = self.head
        while current != None:
            if current.data == x:
                current.data = y
            current = current.next
        return "No such Data"

    def pop_at(self, position):
        if (position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1 and self.head != None):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
        else:
            temp = self.head
            for i in range(1, position - 1):
                if (temp != None):
                    temp = temp.next
            if (temp != None and temp.next != None):
                nodeToDelete = temp.next
                temp.next = temp.next.next
                nodeToDelete = None
            else:
                print("\nThe node is already null.")

MyList = LinkedList()
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()
MyList.push_at(100, 2)
MyList.PrintList()
MyList.push_at(200, 1)
MyList.PrintList()
MyList.pop_at(1)
MyList.PrintList()
print(MyList.search(101))
MyList.update(100, 350)
MyList.PrintList()


