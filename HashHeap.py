class Stack:
    in_queue = []
    out_queue = []
    def push(self, x):
        self.out_queue.append(x)

    def pop(self):
        self.outSafe()
        return self.out_queue.pop(0)

    def top(self):
        self.outSafe()
        return self.out_queue[0]

    def isEmpty(self):
        self.outSafe()
        return len(self.out_queue) == 0

    # help function, make sure out_queue always has 1 latest added element
    def outSafe(self):
        if len(self.out_queue) == 0 and len(self.in_queue) != 0:
            self.out_queue, self.in_queue = self.in_queue, self.out_queue
        while len(self.out_queue) > 1:
            self.in_queue.append(self.out_queue.pop(0))
