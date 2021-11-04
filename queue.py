class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []  

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def print_queue(self):
        print(self.items) 

q = Queue()
q.enqueue ('a')   
q.enqueue ('b')
q.enqueue ('c')
q.enqueue ('d')  

q.print_queue()

q.dequeue()
q.print_queue()            