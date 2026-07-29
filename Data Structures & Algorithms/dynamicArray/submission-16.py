class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = []
        self.size = 0

        for i in range(capacity):
            self.value.append(i)


    def get(self, i: int) -> int:
        return self.value[i]

    def set(self, i: int, n: int) -> None:
        self.value[i] = n

    def pushback(self, n: int) -> None:
        self.value[capacity - 1] = n
        self.size = self.size + 1

    def popback(self) -> int:
        last_value = self.value[capacity - 1]
        self.value[capacity - 1] = None
        self.size = self.size - 1
        return last_value


    def resize(self) -> None:
        for i in range(capacity, capacity * 2):
            self.value[i] = None
        
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
