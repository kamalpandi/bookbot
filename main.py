import re

def count_char(words) -> int:
    all_freq = {}
    words = words.lower()
    words = re.sub(r'[^a-zA-Z]', '' ,words)
    for word in words:
        if word in all_freq:
            all_freq[word] += 1
        else:
            all_freq[word] = 1

    return all_freq


def main():
    with open(f"frankenstein.txt", "r") as f:
        file_content = f.read()
        count = len(file_content.split())
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(count," words found in the document")
        freq = count_char(file_content)
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        for occ,count in sorted_freq:
            print(f"The {occ} character was found {count} times")

        f.close


main()
