class Memory:

    def __init__(self, size):

        self.size = size
        self.data = [0] * size

        self.reads = 0
        self.writes = 0

        self.last_access = None


    def read(self, addr):

        if addr < 0 or addr >= self.size:
            raise Exception("Memory read out of bounds")

        self.reads += 1
        self.last_access = ("read", addr)

        return self.data[addr]


    def write(self, addr, value):

        if addr < 0 or addr >= self.size:
            raise Exception("Memory write out of bounds")

        self.data[addr] = value

        self.writes += 1
        self.last_access = ("write", addr)


    def reset(self):

        self.data = [0] * self.size
        self.reads = 0
        self.writes = 0
        self.last_access = None