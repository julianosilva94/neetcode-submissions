class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.value = [None] * capacity

    def get(self, i: int) -> int:
        return self.value[i]

    def set(self, i: int, n: int) -> None:
        self.value[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.value[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.value[self.size]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.value[i]
        self.value = new_arr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity