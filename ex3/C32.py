class C32:
    def __init__(self):
        self.state = 'A'

    def place(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'C'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'C'
            return 8

    def move(self):
        if self.state == 'B':
            self.state = 'E'
            return (2)
        elif self.state == 'C':
            self.state = 'D'
            return (3)
        elif self.state == 'D':
            self.state = 'D'
            return (6)
        elif self.state == 'E':
            self.state = 'F'
            return (7)