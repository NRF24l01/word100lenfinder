class Letter:
    def __init__(self, let: str):
        self.str = str

    def get_let(self, let: str) -> int:
        if ord(let) > 1077 and not ord(let) == 1105:
            return abs(31 - (ord("я") - ord(let))) + 2
        elif ord(let) == 1105:
            return 7
        else:
            return abs(31 - (ord("я") - ord(let))) + 1


class Word(Letter):
    def __init__(self, word: str):
        self.word = word

    def get_word_sum(self):
        s = 0
        for i in self.word:
            s += self.get_let(i)
        return s


if __name__ == "__main__":
    while True:
        w = Word(input())
        print(w.get_word_sum())
