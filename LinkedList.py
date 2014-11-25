__author__ = 'Pranav Sharma'

class node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

ll = Linkedlist()

def insert(data):
    x = node()
    x.data = data
    if ll.head == None:
        ll.head = node()
        ll.head = x
    else:
        x.prev = ll.head
        ll.head.next = x
        ll.head = x

def delete(data):
    temp = ll.head
    while temp.prev != None and temp.prev.data != data:
        temp = temp.prev
    if temp.prev != None and temp.prev.data == data:
        temp.prev = temp.prev.prev
    else:
        print("No Item Found!!!!")

def printlist():
    temp = ll.head
    while temp.prev != None:
        print(temp.data)
        temp = temp.prev
    print(temp.data)

# Run the script, Enter data, and then 1 to continue entreing data.
# It will automatically display the list
# Then it will ask for deletion
# Again it will display the list.
i = 1
while i == 1:
    print("Enter - ")
    data = int(raw_input())
    insert(data)
    print("Inserted!!Continue ? ")
    #print(data)
    i = int(raw_input())

#print head.prev.data
#head.next.data
printlist()
delete(3)
printlist()
