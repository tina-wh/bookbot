import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

from stats import get_book_text, word_count, char_count, sorted_list

text = get_book_text(book_path)

print ("============ BOOKBOT ============")
print ("Analyzing book found at books/frankenstein.txt...")
print ("----------- Word Count ----------")
print (f"Found {word_count(text)} total words")
print ("--------- Character Count -------")

count = char_count(text)
sorted_counts = sorted_list(count)
for item in sorted_counts:
    if item["char"].isalpha():
        print(f'{item["char"]}: {item["num"]}')

print("============= END ===============")
