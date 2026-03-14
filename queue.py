def __init__(self):
        self.inbox = []   
        self.outbox = []  

    def enqueue(self, x):
        self.inbox.append(x)

    def _transferir(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def dequeue(self):
        self._transferir()
        self.outbox.pop()

    def peek(self):
        self._transferir()
        print(self.outbox[-1])


q = Queue()
n = int(input())

for _ in range(n):
    linea = input().split()
    tipo = int(linea[0])

    if tipo == 1:
        q.enqueue(int(linea[1]))
    elif tipo == 2:
        q.dequeue()
    elif tipo == 3:
        q.peek()
