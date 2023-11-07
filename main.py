from class_data import Word

with open("words.txt", "r", encoding="utf-8") as f:
    words = f.read().split("\n")
    wk = 0
    print(f"Всего слов {len(words)}")
    for i in words:
        w = Word(i)
        wl = w.get_word_sum()
        if wl == 100:
            print(f"Слово: {i}, сумма: {wl}")
            wk+=1
    print(f"Найдено слов: {wk}")