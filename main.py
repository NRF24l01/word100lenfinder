from class_data import Word

with open("words.txt", "r", encoding="utf-8") as f:
    words = f.read().split("\n")
    for i in words:
        w = Word(i)
        wl = w.get_word_sum()
        if wl == 100:
            print("Виха!")
            print(f"Слово: {i}, сумма: {wl}")