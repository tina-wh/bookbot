def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count 

def sorted_list(items):
    char_num = []
    for char, num in items.items():
        char_num.append({"char": char, "num": num})
    char_num.sort(reverse=True, key=lambda d: d["num"])
    return char_num

