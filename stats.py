import re

def get_num_words(words) -> int:
    all_freq = {}
    words = words.lower()
    words = re.sub(r'[^a-zA-Z]', '' ,words)
    for word in words:
        if word in all_freq:
            all_freq[word] += 1
        else:
            all_freq[word] = 1

    return all_freq