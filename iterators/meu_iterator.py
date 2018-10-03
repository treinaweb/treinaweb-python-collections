class MeuIterator:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            resultado = 2 ** self.n
            self.n += 1
            return resultado
        else:
            raise StopIteration

for i in MeuIterator(5):
    print(i)