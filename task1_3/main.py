def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return list_words[min(list(map(len, list_words)))] # используй ключевую у функции min, по которой она долна определять минимальный элемент


if __name__ == "__main__":
    print(task())
