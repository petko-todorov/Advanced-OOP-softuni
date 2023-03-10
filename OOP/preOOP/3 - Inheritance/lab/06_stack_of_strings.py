class Stack:
    data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data):
            return False
        return True

    def __repr__(self):
        return f"[{', '.join(self.data[::-1])}]"


