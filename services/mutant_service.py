class Mutante:
    def __init__(self, dna):
        self.dna = dna
        self.size = len(dna)
        self.mutant_number = 0

    def check_horizontal(self):
        for row in self.dna:
            if self.has_sequence(row):
                self.mutant_number += 1

    def check_vertical(self):
        for col in range(self.size):
            column = "".join([self.dna[row][col] for row in range(self.size)])
            if self.has_sequence(column):
                self.mutant_number += 1

    def check_diagonal(self):
        for row in range(1):
            for col in range(3):
                diagonal_right = "".join(
                    [self.dna[row + i][col + i] for i in range(6 - col)])
                if self.has_sequence(diagonal_right):
                    self.mutant_number += 1

        for row in range(1):
            for col in range(2):
                diagonal_left = "".join(
                    [self.dna[row + 1 + col + i][i] for i in range(5 - col)])
                if self.has_sequence(diagonal_left):
                    self.mutant_number += 1

    def has_sequence(self, row):
        for i in range(len(row) - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                return True
        return False

    def isMutante(self):
        self.check_diagonal()
        self.check_horizontal()
        self.check_vertical()
        if self.mutant_number != 0:
            return True
        else:
            return False
