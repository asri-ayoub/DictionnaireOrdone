class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
            
    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        else:
            state = self.value
            self.value += 1
            return state

if __name__ == "__main__":
    for elt in MyRange(1,9):
        print(elt)