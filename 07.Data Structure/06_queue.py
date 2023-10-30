#Problem : Queue problem (First In First Out)

class Q:

    # Queue creation with empty list
    def __init__(self):
        self.data = []

    # Equeue, append an element to a q
    def enqueue(self,item):
        self.data.append(item)
    
    #Dequeue, pop the first element of the list
    def dequeue(self):
        if len(self.data) != 0 :
            self.data.pop(0)
    
    #Size of the queue
    def qsize(self):
        return (len(self.data))

    #Print queue
    def qprint(self):
        #print(len(self.data))
        print(self.data[::-1])

q = Q()
print("Add 1st element : 10")
q.enqueue(10)
print("Add 2nd element : 20")
q.enqueue(20)
print("Add 3rd element : 30")
q.enqueue(30)
print("Queue elements....")
q.qprint()

print("Pop queue...")
q.dequeue()
print("Queue elements after pop....")
q.qprint()

print("Add 3rd element : 40")
q.enqueue(40)
print("After adding new element, Q elements...")
q.qprint()
