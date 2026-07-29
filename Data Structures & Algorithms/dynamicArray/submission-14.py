class DynamicArray:
    def __init__(self, capacity: int):
        self.value = []

        for i in range(capacity):
            self.value.append(i)


    def get(self, i: int) -> int:
        return self.value[i]

    def set(self, i: int, n: int) -> None:
        self.value[i] = n

    def pushback(self, n: int) -> None:
        last = len(self.value) - 1
        self.value[last] = n

    def popback(self) -> int:
        last = len(self.value) - 1
        last_value = self.value[last]
        self.value[last] = None
        return last_value


    def resize(self) -> None:
        actual_size = len(self.value)
        new_size = actual_size * 2
        
        for i in range(actual_size, new_size):
            self.value[i] = None


    def getSize(self) -> int:
        filled = 0
        
        for i in range(len(self.value)):
            print(self.value[i])
            if self.value[i] is not None:
                filled = filled + 1

        print(filled)
        return filled
        
    
    def getCapacity(self) -> int:
        print(len(self.value))
        return len(self.value)
