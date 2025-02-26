def word_count(text):
    word = text.split()
    count = len(word)
    return count

def char_count(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort(char_count_result):
    char_count_items = list(char_count_result.items())
    char_count_items.sort(reverse=True, key=lambda x: x[1])
    return char_count_items