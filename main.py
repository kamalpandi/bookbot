import sys
from stats import get_num_words

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        
    with open(sys.argv[1], "r") as f:
        file_content = f.read()
        count = len(file_content.split())
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        freq = get_num_words(file_content)
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        for occ,count in sorted_freq:
            print(f"{occ}: {count}")

        f.close


main()
