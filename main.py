def main():
    book_path = "./books/frankenstein.txt"
    text = book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    sorted_list = char_dict_sorted(num_char)

    print(f"------ Begin Report ------\n")
    print(f"{num_words} words found in this book.\n")

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("------ End Report ------")


def sort_num(v):
    return v["num"]


def char_dict_sorted(num_char):
    sorted_list = []
    for char in num_char:
        sorted_list.append({"char": char, "num": num_char[char]})
    sorted_list.sort(reverse=True, key=sort_num)
    return sorted_list


def char_count(text):
    char_dict = {}
    for char in text:
        lower_case = char.lower()
        if lower_case in char_dict:
            char_dict[lower_case] += 1
        else:
            char_dict[lower_case] = 1
    return char_dict


def word_count(text):
    words = text.split()
    return len(words)


def book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
